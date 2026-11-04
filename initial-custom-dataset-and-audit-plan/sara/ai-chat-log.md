# AI Chat Log: TikTok Explore Scraper (method2)

**Tool:** Claude (Anthropic) | **Date:** November 2-3, 2026
**Purpose:** Build a Python script to collect data from the TikTok Explore page as a guest for the custom dataset and audit plan.

## Summary

I asked Claude how to scrape TikTok, then built a Playwright script that opens Explore as a guest, captures the video data TikTok sends to the browser, parses it, removes duplicates, and saves a CSV. I debugged a `NameError`, a captcha block, and scrolling that loaded nothing new, and asked Claude to explain parts of the code. I ended up using only the initial Explore batch (35 videos).

**1. Choosing an approach**
- *Prompt:* "How might I scrape data from TikTok?"
- *Response:* The official Research API is limited to approved academic/nonprofit researchers; other options are third-party services, open-source tools, or TikTok's data export. Unofficial scraping goes against TikTok's terms and raises privacy concerns.
- *Learned:* There is no easy official path for a student project, so volume and data collected need care.

**2. Moving to Playwright**
- *Prompt:* "rather than input a link, I want to go to the TikTok explore page as a guest and get details for the first video"
- *Response:* Explore is JavaScript-rendered, so `requests` can't see it. Claude assisted in creating a Playwright script with a network listener (`page.on("response", ...)`) that captures responses containing `item_list` and parses each video into fields (id, author, views, likes, hashtags, etc.).

**3. Captcha block**
- *Prompt:* "What should I do if I encounter a Captcha?"
- *Response:* Claude declined to help bypass it (solving services, stealth tools, proxies) since that defeats an access control. It suggested solving it manually in the visible browser, waiting before retrying, using the official Research API, or asking my instructor, and documenting the block in the audit plan.

**4. Scrolling and final decision**
- *Result:* 35 videos captured, then "No new videos after 3 scrolls in a row."
- *Response:* The 35 came from the initial page load (my listener was attached before `goto`). 
- *Decision:* I removed scrolling as a method to capture data because it was likely to trigger Tiktok's captcha system, and enough data was coming through the initial page load information.

Overall, I utilized information about Playwright and starter code to build out a usable scraper for an initial load of the Tiktok explore page without distressing the site, and being repeatable realiably.