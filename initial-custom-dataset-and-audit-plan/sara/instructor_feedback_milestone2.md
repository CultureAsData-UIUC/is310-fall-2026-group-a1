# Instructor Feedback for Milestone 2

I think this is a very strong and ambitious submission. I appreciate how substantially you revised the project after discovering that you could collect structured data from TikTok’s Explore page. 

I also appreciated that you are not simply measuring which videos are popular, but investigating what TikTok repeatedly presents as popular to a guest user and what that collection process allows us to know about platform curation. The repeated videos, changing engagement counts, missing hashtags, access restrictions, and dependence on a particular time, location, and IP address are not merely technical complications. They are fascinating evidence about how the platform and your collection method shape the dataset!

## Initial Custom Dataset

I appreciate that you collected more data than you needed too and that you had a well documented dataset dictionary in your README. For the next milestone, you might consider expanding this existing table where additional context would help readers interpret or reuse the data. In particular, you might consider documenting:

- The data type and unit of each field
- Whether the field describes the video or the collection event
- Whether its value can change over time
- What a blank or missing value means
- Any transformations performed by the scraper
- Any uncertainty about how TikTok defines or calculates the value

The `created` field records when a video was posted, but the dataset does not record precisely when each row was collected. That distinction is essential because views, likes, comments, shares, and saves change over time. So you might add fields like `collected_at`, `collection_run`, as well as documenting the relevant time zone. The current conversion of TikTok timestamps uses the computer’s local time zone, so the meaning of the displayed posting time should be made explicit.

You describe the collection as coming from a “fresh account,” but the scraper actually opens TikTok as a guest rather than using a newly created account. It's not exactly clear how much that might differ the data, but worth being specific in your language. 

### Duplicate Videos and the Shape of the Data

I think the repeated videos are one of the most interesting findings in the submission, but I think you could use a bit more clarity around how you are defining duplication. 

Specifically, the notebook uses `drop_duplicates()` across complete rows, which removes 69 exactly identical rows and produces a file with 155 rows. However, that cleaned file still contains:

- 112 unique video IDs
- 27 video IDs that appear more than once
- 43 additional rows produced by repeated video IDs

These rows remain because engagement metrics changed between collection runs. For example, the same video can have slightly different numbers of likes, comments, shares, or saves in different rows. This means that the repeated records may represent temporal snapshots rather than simple duplicate data.

Which means you need to decide what one row in the final dataset should represent. If one row represents one unique video, deduplicate using `video_id` and explain whether you retain the first, last, or another observation. If one row represents one video at one collection moment, preserve the repeated observations but add collection timestamps and run identifiers. The second option could support an interesting analysis of how metrics changed, but the current data does not record enough information to distinguish the collection events reliably.

Clarifying this question might also help you reconsider how you are calculating that approximately 29% of the records were duplicates. That percentage describes rows that were identical across every field. If duplication is defined by repeated video ID, half of the raw rows are repeated occurrences. Both measurements can be useful, but they represent different concepts and should be named clearly.

## Documentation and Computational Work

I really like your use of the Playwright scraper and appreciated that you were thoughtful in your documentation of your processes in both your README and AI log. However, the repository could benefit from clearer instructions for reproducing the collection. So I would suggest that you add:

- Installation instructions for Python dependencies and Playwright’s Chromium browser
- The command used to run the scraper
- The expected output location
- A warning that TikTok may return a CAPTCHA or different page structure
- An explanation that repeated runs append to the same file. Relatedly, the code comments that it “overwrites” the existing file, but `save_csv()` opens the file in append mode, so you could correct that as well.
- The intended procedure for starting a new collection
- The order in which the scraper and cleaning notebook should be run
- The Python and package versions used, where relevant

The notebook also writes `output_file.csv`, while the repository contains `cleaned_explore_videos.csv`. I would suggest making the notebook, filenames, and documentation consistent so another user can reproduce the published output.

Also a small note but the script does not technically bypass a CAPTCHA; it captures the initial structured response and stops or waits when TikTok presents an access challenge. You might update the documentation to describe this as a collection method designed to minimize requests and respect access controls, not as a way to evade them. Just a suggestion though!

### Ethics, Privacy, and Data Access/Reuse

I noticed that dataset includes public usernames, video identifiers, descriptions, and engagement metrics. I think it would be helpful to more directly address your choices of what to include or not. In particular, I'm wondering if you are considering not including certain videos because it might involve more vulnerable populations. I do think it might be helpful to consider going to profiles to ensure that you aren't bringing attention to users that might not be as public. 

I appreciated that you kept both the raw and cleaned datasets, but it would also be useful to make the naming and transformation process clearer of which is which. I would also encourage you to write in your final essay about how the transient nature of the platform presents challenges for data reuse as well. 

## Audit Plan & Considerations

I like your idea of auditing TikTok though as you note there is a number of limitations in accessing that data. Since you are not auditing a separate dataset, I would ask that you collect a bit more data for your custom dataset, so that you are confronting the issue of scale. 

I also would suggest digging a bit more into Playwright tool and its origins, as well as interpretative choices about what and how to collect this data.

I also think it would be helpful to think about how you might dig into hashtags to support your pivoted focus to the Explorer page popularity. The cleaned file includes 304 unique hashtag values, with `fyp`, `viral`, `funny`, and `asmr` among the most frequent. However, 32 rows in the cleaned file have no hashtags. I would recommend treating that absence as part of the analysis rather than simply removing those videos. 

The bigger next step is adding more of your own subjectivity into the data. I would consider maybe thinking about generating your own categorization of why a video is popular. It could be based on trends across the dataset, but also your own almost speculative theory of what is happening on the platform. 

I think this would be particularly interesting approach since you have duplicate videos, so you don't have to categorize every video but maybe focus on some of the most frequently repeated videos in the dataset. 

I liked your use use of the McNulty and Pew Research sources, and especially how it relates to the data restrictions with TikTok. I think you might look for another two or three citations that are more focused on the Explorer page. Happy to help you find citations if you are struggling! 

## Priorities for Milestone 3

- Decide whether one row represents a unique video or a video observed during a particular collection run, which might impact the duplicate-removal process and how you document repeated rows as temporal observations.
- Add collection timestamps, run identifiers, time zones, and page position when available.
- Conduct several documented collection runs to investigate variation over time.
- Develop transparent interpretive categories for a focused sample of frequently repeated videos.
- Treat repeated videos and missing hashtags as findings rather than removing them.
- Reconcile filenames and raw, cleaned, observation-level, and unique-video counts.
- Document field definitions, Playwright’s role, access restrictions, and the collection workflow.
- Address creator privacy, platform transience, and responsible reuse.
- Potentially add scholarship on recommendation systems and the limits of inferring algorithms from platform outputs.
