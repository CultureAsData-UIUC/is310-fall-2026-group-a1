# Instructor Feedback for Milestone 2

I like that you narrowed the project to a concrete sample of 50 songs from the Billboard Hot 100 to look at the impact of major labels and hit making. Your initial result is striking: all 50 songs connect to a major music company. However, I'm wondering whether your approach is simply surfacing we already know about major labels and I'm wondering why not look for songs specifically that are not from major labels in the Billboard Hot 100. 

I did appreciate that you noticed the underlying situation is more complicated than the major labels suggest. Your discussion of subsidiaries, joint releases, and distribution relationships identifies what may ultimately be the project’s most interesting cultural question: what does it actually mean for music to be “independent” in an industry where ownership, distribution, promotion, and release credits may involve several companies?

## Initial Custom Dataset

Your README explains that songs released through multiple labels were assigned to whichever major company owned or worked with one of those labels. That gives you a countable category, but the current CSV only preserves the final classification. A future researcher cannot see the original label credits, the smaller label involved, the ownership or distribution relationship, or the evidence you used to make the classification.

I would suggest expanding the dataset with fields such as:

- Billboard rank
- URL to the web page
- Chart date
- Label credit exactly as Billboard presents it
- Individual labels involved
- Parent company, where applicable
- Distribution company, where applicable
- Major, independent, or uncertain classification
- Evidence source for the ownership or distribution relationship
- Notes explaining ambiguous cases

You might also retain several fields rather than forcing every song into a single company. For example, a release could involve an artist-owned imprint, an independent label, and a major distributor at the same time. Preserving those layers would let you ask how independent cultural production becomes connected to major-label infrastructure rather than treating “independent” and “major” as completely separate categories.

### Dataset Documentation and Provenance

The current file has three columns: song name, label, and artist. Those fields are understandable, but the dataset needs more documentation about where and when the records were collected. Since the Hot 100 changes every week, the chart date is essential to interpreting the sample. It would also help to include the chart rank and links to the Billboard chart and label evidence.

I would recommend adding a data dictionary that defines each field and explains how you classified releases. In particular, your final documentation should make clear whether the `Label` field represents the label printed by Billboard, the ultimate parent company, or your own researched classification. Right now, the README suggests that it represents the final parent-company classification, but the column name alone does not communicate that distinction.

Your discussion also refers to the “current top 50,” but data should ideally record an exact date rather than rely on a relative description such as “current.” This will make the dataset reusable after the chart changes.

### Strengthening the Cultural Question

Your finding that every song in the top 50 has major-label backing is meaningful, but it does not necessarily tell us that independent artists cannot achieve prominence. It tells us something more specific about which releases reached the top half of Billboard’s Hot 100 during one particular week.

You might therefore frame the project around questions such as:

- What kinds of label and distribution relationships sit behind songs presented as individual artist releases?
- How much apparent label diversity remains after tracing companies to their parent corporations?
- Where, if anywhere, do releases without major-company involvement appear on the full Hot 100?
- Does the chart make complicated production and ownership relationships visible or collapse them into a simple label credit?
- How does Billboard’s method for measuring popularity advantage particular forms of distribution, promotion, or platform visibility?

Expanding to the full Hot 100 could be useful because it would let you test your hypothesis that independent releases appear lower on the chart. I would suggest doing that before adding many additional weeks. One complete chart with richer ownership and distribution metadata may produce a more meaningful analysis than a much larger dataset containing only artist, song, and simplified parent label.

## Audit Plan

The README mentions an existing online dataset that you may combine with your records, but it does not identify or link to that dataset. For the audit, you should detail the exact dataset and investigate its provenance before combining it with your work.

You might consider asking:

- Who created the dataset, and how did they obtain the Billboard records?
- Does each row represent a song, a weekly chart appearance, or something else?
- Which years and chart positions are included?
- Are repeated appearances of the same song preserved?
- What fields are missing?
- Are label names included, and do they represent release labels, distributors, or parent companies?
- Can selected records be verified against Billboard or another source?
- What transformations would be necessary before it could be compared with your dataset?

This audit could become especially productive if the existing dataset preserves Billboard’s original label information. You could then add your researched ownership classifications while keeping the source values intact.

## Computational Work

You explain that the initial dataset was created manually in a spreadsheet and that you did not use computational tools. While you submitted the results as a CSV, Milestone 2 also requires a computational artifact and a reproducible computational process rather than using spreadsheet software. You might for instance create a data entry interface whether an HTML page or Python CLI script. You could also alternatively create a Jupyter notebook for analyzing and visualizing the data, especially once you scale up the size of your data with the audit.

Another option would be using web scraping to help collect chart records. But generally, I think the most interesting computational challenge may be matching label names, preserving relationships among companies, and checking your classifications against documented sources, so happy to help brainstorm how you might integrate computation!

## Scholarship and Reflection

The submission does not yet include the required published scholarship. I would suggest finding work on the recorded music industry, corporate consolidation, independent labels, Billboard chart methodology, streaming, or music distribution. Scholarship can help you determine whether “major versus independent” is the most useful distinction or whether ownership, distribution, promotion, and platform access should be considered separately.

Your reflection identifies some useful surprises, particularly the complete absence of clearly independent releases from the top 50 and the frequency of joint label relationships. I would build from those discoveries. Rather than treating complicated credits as an inconvenience that needs to be simplified, you might make that complication central to the project.

## Priorities for the Final Project & Milestone 3

- Expand one chart week to the full Hot 100 before collecting additional weeks so you can investigate whether releases without major-company involvement appear lower in the rankings.
- Preserve Billboard’s original label credits alongside separate fields for imprints, parent companies, distributors, joint releases, and uncertain relationships.
- Add chart rank, exact chart date, source links, classification evidence, and notes about ambiguous cases.
- Create a data dictionary that distinguishes source values from your researched classifications.
- Identify and audit the existing Billboard dataset before combining it with your records.
- Add a reproducible computational artifact for collecting, matching, validating, analyzing, or visualizing the data.
- Add scholarship on music-industry consolidation, independent labels, distribution, streaming, or Billboard’s chart methodology.
- Limit conclusions to the chart week and positions represented while making complicated ownership and distribution relationships central to the analysis.

You have found a strong initial pattern. The opportunity now is to investigate the corporate relationships hidden beneath these charts, while making your classification process visible to readers.
