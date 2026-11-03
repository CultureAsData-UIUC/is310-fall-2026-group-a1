import csv
import json
from datetime import datetime
import os

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from rich.console import Console
from rich.table import Table
import random


# Constants --------------------------------
EXPLORE_URL = "https://www.tiktok.com/explore"
REQUEST_DELAY = 2  # seconds

#Self Identification -----
USER_AGENT = "is310-course-scraper/1.0 (student project; sjohn241@illinois.edu)"

# Set up console for rich console
console = Console()

# Global Vars --------------------------------------
recorded_videos = []  # raw video objects TikTok sends while the page loads

# Helper Functions ----------------------------------
def parse_item(item):
    """Turn a TikTok video object (from the API or page JSON) into a flat dict."""
    stats = item.get("stats", {})
    author = item.get("author", {})
    music = item.get("music", {})
    hashtags = [t.get("hashtagName") for t in item.get("textExtra", []) if t.get("hashtagName")]
    created = item.get("createTime")

    return {
        "video_id": item.get("id"),
        "author": author.get("uniqueId") if isinstance(author, dict) else author,
        "description": item.get("desc"),
        "created": datetime.fromtimestamp(int(created)).strftime("%Y-%m-%d %H:%M") if created else None,
        "duration_sec": item.get("video", {}).get("duration"),
        "views": stats.get("playCount"),
        "likes": stats.get("diggCount"),
        "comments": stats.get("commentCount"),
        "shares": stats.get("shareCount"),
        "saves": stats.get("collectCount"),
        "music": music.get("title"),
        "hashtags": ", ".join(hashtags),
    }

def video_from_detail_page(page, href):
    """Fallback: open a video's own page and read the JSON embedded in it."""
    page.goto(href, wait_until="domcontentloaded")
    raw = page.locator("#__UNIVERSAL_DATA_FOR_REHYDRATION__").inner_text(timeout=15000)
    data = json.loads(raw)
    item = data["__DEFAULT_SCOPE__"]["webapp.video-detail"]["itemInfo"]["itemStruct"]
    return parse_item(item)

# Display collected data for a test open
def show_video(video):
    table = Table(title="First video on TikTok Explore")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="white")
    for key, value in video.items():
        table.add_row(key, str(value))
    console.print(table)

# Save video information (overwrites exisiting file)
def save_csv(videos, filename="explore_videos.csv"):
    #check if file exists and is populated
    file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=videos[0].keys())
        if not file_exists:    #update header if not present
            writer.writeheader()
        writer.writerows(videos)
    console.print(f"[green]Saved {len(videos)} video(s) to {filename}[/green]")

# Listens for network traffic from Tiktok
def on_response(response):
            # Explore feed data arrives from endpoints with "item_list" in the URL
            if "item_list" in response.url:
                try:
                    data = response.json()
                except Exception:
                    return
                recorded_videos.extend(data.get("itemList", []))



def main():
    recorded_videos.clear() # just in case

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1280, "height": 900},
            locale="en-US",
        )
        page = context.new_page()
        page.on("response", on_response)

        console.print("[cyan]Opening TikTok Explore as a guest...[/cyan]")
        page.goto(EXPLORE_URL, wait_until="domcontentloaded")

        # captcha handling
        try:
            page.wait_for_selector('a[href*="/video/"]', timeout=20000)
        except PlaywrightTimeout:
            console.print("[yellow]Possible captcha. Solve it in the browser window; waiting up to 2 minutes...[/yellow]")
            try:
                page.wait_for_selector('a[href*="/video/"]', timeout=120000)
                # Reload so the feed request fires again with the listener attached
                page.reload(wait_until="domcontentloaded")
                page.wait_for_selector('a[href*="/video/"]', timeout=20000)
            except PlaywrightTimeout:
                console.print("[red]Still no videos. Giving up.[/red]")
                browser.close()
                return

        page.wait_for_timeout(3000)  # let the initial feed requests finish

        
        # Fallback if the network listener captured nothing
        fallback_video = None
        if not recorded_videos:
            console.print("[yellow]No feed data captured, falling back to the first video link...[/yellow]")
            href = page.locator('a[href*="/video/"]').first.get_attribute("href")
            if href:
                fallback_video = video_from_detail_page(page, href)

        browser.close()

    # Parse and de-duplicate by video id
    videos = []
    seen_ids = set()
    for item in recorded_videos:
        vid = item.get("id")
        if vid and vid not in seen_ids:
            seen_ids.add(vid)
            videos.append(parse_item(item))

    if fallback_video:
        videos.append(fallback_video)

    if videos:
        show_video(videos[0])  # still shows the first one as a test display
        save_csv(videos)
    else:
        console.print("[red]Could not get video details.[/red]")

# Only run when executing file directly
if __name__ == "__main__":
    main()