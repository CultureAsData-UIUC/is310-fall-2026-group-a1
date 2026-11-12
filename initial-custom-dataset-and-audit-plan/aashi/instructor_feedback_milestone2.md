# Instructor Feedback for Milestone 2

Overall, I like the project’s focus on differences in reception between critics and audiences and across platforms. The care you have taken to match movie titles and metadata across datasets is particularly valuable. That matching process could become an important part of the project’s methodological contribution.

The project now needs a clearer account of what each platform’s ratings measure, more complete dataset documentation, and a more focused audit plan. These revisions will help turn the collection from an assortment of platform metrics into a meaningful investigation of how movie reception is constructed and represented.

## Initial Custom Dataset

The 2015–2024 date range makes sense, but I am wondering whether 60 films creates too many comparisons to interpret closely. You might retain all 60 films for identifying broad patterns while selecting a smaller, intentionally chosen subset for closer analysis. This subset could include films with especially large critic–audience disagreements, substantial differences across platforms, or contrasting patterns in their written reviews.

I also appreciate your transparency about removing records with missing ratings. However, you should investigate whether this decision changed the sample in systematic ways. Were particular genres, years, platforms, or kinds of films more likely to be removed? Missingness may itself provide evidence about which films receive coverage on these platforms.

Before comparing ratings, you also need to establish whether the measures are comparable. Are you comparing averages, percentages of positive reviews, critic scores, audience scores, or different combinations of these measures? Even if the values can be converted mathematically to a common scale, they may represent different concepts and populations. In many ways, this is the central issue in your dataset, so consider how you can surface the differences among ratings, percentages, and rankings rather than treating them as interchangeable.

## Documentation and Computational Work

I appreciate that you worked with Pandas, included your scripts, and described the purpose of the files. However, the dataset needs more complete documentation. Please add a data dictionary explaining:

- What every field represents
- Which platform or dataset provided it
- The relevant scale or unit
- How each value was collected or calculated
- What missing values mean
- Which transformations you performed
- Which fields contain your own interpretations rather than source data

You should also document the title-matching process more fully. Matching titles and metadata across platforms requires important interpretive decisions. Explain which fields you used, how you identified incorrect matches, how you corrected them, and how confident you are in the remaining matches.

There also appears to be a discrepancy in the review-selection method. The README says that one review was selected randomly, but the code sorts qualifying reviews by length and then retains the first review for each movie. This appears to select the longest qualifying review rather than a random review. Please clarify which method you intended to use and make the code and documentation consistent.

This passage in the README was also unclear:

> Rotten Tomatoes looks at the number of positive ratings, and Letterboxd looks at star ratings, and the Letterboxd average comes from just a sample of users not the whole platform.

Why is the Letterboxd average described as a sample while the Rotten Tomatoes measure is not? What does “the number of positive ratings” mean here: a count, a percentage, or the platform’s displayed score? What does each platform expose publicly, and how does each platform calculate the displayed value? It might be tricky to answer but I would encourage you to at least take a look at and potentially cite the relevant platform to help clarify what each field/platform represents.

### Review Annotation Framework

I really liked how you decided to include your subjectivity through the review annotations and you have an impressive number of categories. While these categories show careful engagement with the reviews, they currently mix several analytical levels:

- Formal features such as acting, pacing, characterization, and visual style
- Emotional or audience responses such as entertainment value and emotional impact
- Genre judgments such as suspense, humor, and genre expectations
- Evaluative judgments such as originality
- Subject matter grouped under the general category “themes”

The “themes” category is especially broad. It includes observations about war, race, grief, sexual violence, friendship, business, and family relationships. You might consider either breaking it into more specific categories or providing a clearer explanation of what qualifies as “themes” rather than another category.

In the final data essay, I would also encourage you to narrate the annotation process through concrete examples. You might reproduce a short excerpt or summary from a review, show the category you assigned, and explain why you made that choice. Including both straightforward and ambiguous examples so readers can understand the interpretive method.

You might also add a field that records uncertainty. This could use values such as `high`, `medium`, or `low` confidence, or it could contain a note explaining why a review was difficult to categorize. Recording uncertainty would be especially useful when a review could reasonably fit several categories. Rather than forcing every review into one definitive theme, uncertainty can become part of the data and the project’s argument about interpretation.

## Audit of the Existing Datasets

For the audit, I would not recommend adding another platform or source dataset. Instead, I would highly suggest that you focus on auditing the **full datasets you have already used**, not only the final sample of 60 films.

Where did each dataset actually come from? Who created and released it? How was it collected? What is present, what is missing, and why? These should be the central questions for the next stage of your audit.

Begin by investigating the complete Rotten Tomatoes ratings dataset, Letterboxd ratings dataset, and Rotten Tomatoes critic reviews dataset. The people who published these datasets are not necessarily affiliated with the platforms that originally produced the data. For each dataset, determine:

- Who created and published it
- How and when it was collected
- What one row represents
- Whether it contains complete platform data or a sample
- Which films, critics, users, ratings, or reviews are included
- Which fields contain missing values and whether that missingness follows any patterns
- Whether duplicate records or identifiers are present
- What transformations may have occurred before you downloaded it
- What its license permits you to reproduce or redistribute

Use code to examine the full shape and coverage of these datasets. This could include row counts, field names, date ranges, missing-value counts, duplicate records, rating distributions, and the number of films or reviews that can be matched across sources. The goal is not necessarily to correct every problem. The goal is to understand and document the data’s provenance, structure, coverage, and limitations.

You should then audit how your own process transformed those larger datasets into the 60-film sample. Record how many records remained after each step, including:

- Removing duplicate records
- Restricting the date range
- Requiring at least 25 Letterboxd ratings
- Removing films with missing ratings
- Matching titles across platforms
- Correcting erroneous matches
- Dividing films into reception categories
- Selecting 20 films from each category
- Matching films to available critic reviews

This will help you identify whether the final sample systematically privileges certain films and excludes others.

## Scholarship and Reflection

I appreciate that you have already considered several limitations. The next step is to connect relevant scholarship about platforms, ratings, reception, review aggregation, or recommendation systems to specific methodological decisions. Scholarship could help you explain why platform metrics are not neutral representations of audience opinion and why apparently comparable scores may encode different populations and practices.

The interpretive review categories also provide an opportunity for reflection. Discuss how your own expectations shaped the categories, which reviews resisted classification, and how recording uncertainty changed your understanding of the annotation process. You might bring in some of our course readings to inform these choices, and also happy to help you find relevant citations.

## Data Access and Reuse

I appreciate that you did not redistribute restricted raw data, but the documentation should still link to the original sources or explain precisely how an authorized reader could locate them.

Clearly distinguish among:

- Data you are permitted to share
- Restricted data that you cannot redistribute
- Data you derived or transformed yourself
- Manual annotations you created
- Documentation and code that can be published

Explain how another researcher could reproduce the dataset from the linked sources, including any access requirements and the sequence in which the scripts should be run.

## Priorities for Milestone 3

- Audit the complete Rotten Tomatoes ratings, Letterboxd ratings, and Rotten Tomatoes reviews datasets. Document who created each dataset, how it was collected, what one row represents, and whether it is complete or sampled. Examine the full datasets for missing values, duplicates, coverage, date ranges, and other structural patterns.
- Clarify how each platform calculates its ratings and whether the measures are comparable. 
- Investigate how removing missing values and requiring at least 25 Letterboxd ratings affected the film sample. Document how every filtering and matching step changed the number and kinds of records in the working dataset. Clarify and document how the reviews were selected.
- Reconcile the documented review-selection method with the code.
- Add dataset documentation, a data dictionary, and access instructions for the original sources. 
- Create a transparent annotation documentation with definitions and examples. Explain how reviews with multiple possible themes are handled. Consider recording secondary themes and coding uncertainty. Include straightforward and ambiguous coding examples in the final data essay.

Overall, this is a promising comparative dataset with a clear focus on differences between critic and audience reception. The strongest next step is to audit the source datasets and make the thematic coding process more transparent so that the final analysis can distinguish meaningful reception patterns from the effects of platform scales, missing data, matching, and review selection.