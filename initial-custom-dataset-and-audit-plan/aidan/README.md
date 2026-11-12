# Initial Custom Dataset and Audit Plan

### Author: Aidan Lueken

## Dataset Fields

This dataset was created by collecting Reddit comments discussing Dungeons & Dragons 4th Edition (D&D 4e) and Pathfinder. The dataset is intended to examine how tabletop roleplaying communities discuss different editions of games, particularly in relation to mechanics, combat, complexity, customization, and the overall player experience.

The current dataset contains **54 comments**, consisting of 31 comments from a D&D 4e discussion and 23 comments from a Pathfinder discussion. Comments were collected from Reddit discussion threads and manually organized into a CSV file.

| Text                 | Raw                    | Description of Field                                                       |
| -------------------- | ---------------------- | -------------------------------------------------------------------------- |
| Index                | `index`                | Sequential index assigned to each row of the dataset                       |
| Comment ID           | `id`                   | Unique identifier assigned to each comment in the dataset                  |
| Subreddit            | `subreddit`            | Reddit community where the discussion originated                           |
| Post ID              | `post_id`              | Identifier of the original Reddit discussion                               |
| Edition Focus        | `edition_focus`        | Tabletop RPG edition or comparison discussed by the comment                |
| Comment Text         | `comment_text`         | Original Reddit comment text collected for analysis                        |
| Sentiment            | `sentiment`            | Coded sentiment of the comment toward the edition or topic being discussed |
| Sentiment Confidence | `sentiment_confidence` | Confidence level assigned to the sentiment annotation                      |
| Themes               | `themes`               | Main topics or themes identified within the comment                        |
| Annotation Note      | `annotation_note`      | Additional notes explaining or contextualizing the annotation              |
| Source URL           | `source_url`           | URL of the Reddit discussion from which the comment was collected          |
| Collection Method    | `collection_method`    | Method used to obtain the comment                                          |
| Reddit Score         | `reddit_score`         | Reddit score associated with the comment, when available                   |
| Reddit Author        | `reddit_author`        | Reddit username associated with the comment, when available                |
| Reddit Timestamp     | `reddit_timestamp`     | Timestamp associated with the comment, when available                      |
| Parent Comment ID    | `parent_comment_id`    | Identifier of the comment that the comment replies to, when available      |
| Sentiment Annotator  | `sentiment_annotator`  | Person or process responsible for assigning sentiment                      |

## Revised Proposal

My project focuses on examining how Reddit users discuss different editions of tabletop roleplaying games, particularly Dungeons & Dragons 4th Edition and Pathfinder. Rather than examining popularity through numerical engagement metrics like I attempted to do before, I am interested in the ways players describe their experiences with different systems and the cultural preferences that emerge from these discussions.

The dataset contains discussions about the advantages and disadvantages of different game editions. These include arguments concerning tactical combat, class differentiation, character customization, game complexity, accessibility, roleplaying, and the influence of video games on tabletop design.

My primary research interest is understanding what players value in tabletop roleplaying systems and how those preferences influence the reception of different editions. I am particularly interested in examining whether discussions about game editions are shaped by disagreements over complexity, accessibility, mechanical depth, and what players believe a tabletop roleplaying game should be.

## Collecting & Structuring Cultural Data

**Platform: Reddit**

I collected comments from Reddit discussions concerning D&D 4th Edition and Pathfinder. The comments were organized into a structured CSV dataset, with each comment represented as an individual row.

The dataset currently consists of two discussion groups:

- D&D 4th Edition: 31 comments
- Pathfinder: 23 comments

This produces a combined dataset of 54 comments.

The comments were collected from discussion threads and organized into a CSV file. I preserved the original comment text so that the dataset could be used for qualitative analysis and future computational analysis. Each comment also includes information about its source discussion and, where available, metadata associated with the Reddit comment.

In addition to collecting the comments, I structured the dataset around several analytical fields. Sentiment annotations allow comments to be categorized according to their general attitudes, while themes allow comments to be grouped according to the topics they discuss. These fields make it possible to examine the dataset through both qualitative reading and computational methods.

The dataset is stored in `combined_reddit_dataset_updated.csv`, which contains both the D&D and Pathfinder comments in one file.

## Audit and Connection Plan

The platform I am examining is Reddit. Reddit is particularly useful for this project because its discussion-based structure allows players to communicate their opinions, respond to disagreements, and explain their experiences with different tabletop roleplaying systems.

My dataset provides an opportunity to examine how these discussions reflect broader cultural preferences within tabletop gaming communities and see how popularity can be viewed through the lens of infamy. However, the dataset is limited to a small number of selected discussions and should not be treated as representative of all Reddit users or tabletop roleplaying players.

One important consideration is that Reddit comments are publicly accessible but were written by individuals participating in discussions. Their public availability does not eliminate ethical considerations associated with collecting and analyzing user-generated content. I intend to preserve the context of comments, avoid unnecessary identification of individual users, and focus my analysis on discussion patterns rather than individual identities.

The dataset also presents an opportunity for auditing through comparison with other sources of cultural data. For example, I could compare the themes identified in Reddit discussions with discussions of tabletop RPG editions on other platforms or with existing research on online gaming communities. This could help identify whether the attitudes present in my dataset are specific to these Reddit discussions or reflect broader patterns within tabletop gaming culture.

For analysis, I plan to use Python and libraries such as pandas and matplotlib to examine the distribution of sentiment and themes across the two discussion groups. Visualizations could help illustrate the frequency of different topics, the distribution of sentiment annotations, and differences in how users discuss particular editions.

## Reflection

The dataset provides a useful foundation for qualitative analysis because the original comment text is preserved. This allows me to examine the reasoning behind individual opinions rather than relying exclusively on numerical sentiment scores or engagement metrics.

One limitation is the relatively small size of the dataset. With only 54 comments collected from two discussions, the findings will primarily represent the perspectives expressed within those specific threads. Additionally, sentiment and theme annotations involve interpretive decisions that may introduce subjectivity into the analysis.

## Sources

- Reddit D&D 4th Edition discussion: [https://www.reddit.com/r/DnD/comments/1dsibb7/why_is_4th_edition_so_hated/](https://www.reddit.com/r/DnD/comments/1dsibb7/why_is_4th_edition_so_hated/)
- Reddit Pathfinder discussion: [https://www.reddit.com/r/Pathfinder/comments/1p6c08o/pathfinder_1e_vs_2e_complexity/](https://www.reddit.com/r/Pathfinder/comments/1p6c08o/pathfinder_1e_vs_2e_complexity/)