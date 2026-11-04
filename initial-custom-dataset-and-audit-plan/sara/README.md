
# Initial Custom Dataset and Audit Plan
### Author: Sara Johnson

## Dataset Fields 

The fields here were determined after examining the data present when web-scraping the Tiktok Explore page on a fresh account . All initial data was scraped on 11/3/2026 from 12:00pm - 1:00pm.

| Text | Raw | Description of Field |
| -------- | -------- | -------- |
| Video  | 'video_id'   | Id of the Video; Can be used with author to find specific videos  |
| Author   | 'author'  | Username/Creator of the video   |
| Description   | 'description'   | Description of the video  |
| Created   | 'created'   | Time when video was posted to the platform   |
| Video Duration   | 'duration_sec'  | Duration in seconds of the video   |
| Views   | 'views'   | Number of views at time of collection (see below)   |
| Likes   | 'likes'   | Number of likes on the video at time of recording (see below)  |
| Comments   | 'comments'   | Number of comments on the video at time of recording (see below)  |
| Shares   | 'shares'   | Number of shares on the video at time of recording (see below)   |
| Saves   | 'saves'   | Number of saves on the video at time of recording (see below)   |
| Music   | 'music'  | Background audio used in the video - listed as original sound if one is not used  |
| Hashtags   | 'hashtags'   | List of hashtags attached to the video (which may also be present in the description)  |

*This data was collected on 11/3/2026 at 12:00pm - 1:00pm.*

---

## Revised Proposal

I have updated the topic of my proposal to mainly center around the platform Tiktok. One reason for this is that there are currently no relevant collections of data for Tiktok on Kaggle, and everywhere else I tried to search (that are well documented). 

When I have collected initial data from the platform, I am going to analyze popularity on Tiktok, mainly by examining what types of videos, hashtags, and content comprise the videos on a new user's Explore page. I would also like to examine the impact of video duration on content type and popularity.

## Collecting & Structuring Cultural Data
Platform: Tiktok

I used [Playwright](https://playwright.dev/) with Chromium to open a guest instance of the Tiktok Explore page. I made sure to identify myself through the user_agent parameter.

Once the instance of Chromium is launched, I had the scraper capture page responses sent as the page loaded in, then closed the instance of Chromium. Each pass of the tool typically yielded around 25-35 video links which I could then pursue and scrape for statistics. 

I used this method because doing so allowed the scraper to avoid encountering the Captcha. When the Tiktok explore page opens for a guest, it opens immediately to a video. To avoid affecting the algorithm by pausing on a potential Captcha or other screen (such as the mandatory birthday input for guest users), this method was the cleanest. 

This method also yielded some interesting additional information. Around 67 of the original 224 videos collected were duplicates in the raw data, which is around 29% total. This could point to there being specifically curated videos (or a curation formula) for the Explore page for all new users. The alternate explanation is that my computer, which carries my IP and location was being served similar videos. However, both theories give us an another initial insight into popularity on the site.

I've removed duplicates using a simple Jupytr notebook (quickremove.ipynb in the dataset folder) and put a csv of unique videos in the same folder.

## Audit and Connection Plan

The platform I will be auditing is Tiktok. While Tiktok does have an official API, it is only accessible to researchers and must be applied to. Hopefully by making my method of scraping public, I will contribute to more accessible research methods for this platform. The findings regarding popularity from this data will help me understand the culture behind popularity on the 5th most popular social media platform globally.

In "What's on Top of Tiktok", McNulty discusses how Tiktok's API "remains largely untested in published research due to foreboding terms of service", meaning that it is tricker to collect data from these platforms for research. And yet, they also mention in the same article how if we don't have access to this data, we have no idea what people are spending hours of their lives doing on these platforms. My project is already bridging this gap by providing an avenue for collecting data from Tiktok. 

According to the Pew Research Center's "Teen's Experiences on Tiktok", teens are regularly using the platform for things like 'product reviews, 'entertainment', 'keeping up with celebrities', and 'keeping up with politics'. With young people using the platform for this purpose, I am interested as well how a platform such as Tiktok, which functions differntly to other platforms in that it serves videos to users instead of having them search for them, can influence these activities.

Now that I have collected my data, I plan to use data visualization tools and libraries such as matplotlib and pandas to create charts that help to model and explain findings regarding popularity on platforms. 

Sources:
- https://www.publicbooks.org/whats-on-top-of-tiktok/
- https://www.pewresearch.org/internet/2026/04/15/teens-experiences-on-tiktok-instagram-and-snapchat/

## Reflection

What is working on my project is that I was able to scrape the data off of Tiktok successfully. The scope of my original proposal was made with the assumption I would not be able to scrape this data, so now I am able to adjust it more appropriately. I will be adjusting the direction of the project to be centered around modeling and understanding actual metrics behind popular videos on the Explore page, rather than just focusing on humor. 