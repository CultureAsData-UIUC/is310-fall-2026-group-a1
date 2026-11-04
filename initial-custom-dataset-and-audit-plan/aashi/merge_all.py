
import pandas as pd

movies = pd.read_csv("output/movie_annotations.csv")
reviews = pd.read_csv("output/selected_reviews.csv")
annotations = pd.read_csv("data/review_annotations.csv")

movies["rt_id"] = movies["url"].str.split("/m/").str[-1]

movies = movies.drop(columns=[
    "review_url",
    "review_sentiment",
    "review_theme",
    "review_observation",
    "annotation_status"
], errors="ignore")

reviews = reviews[[
    "rt_id",
    "reviewText",
    "reviewUrl",
    "scoreSentiment",
    "criticName"
]]

reviews = reviews.rename(columns={
    "reviewText": "review_text",
    "reviewUrl": "review_url",
    "scoreSentiment": "review_sentiment",
    "criticName": "critic_name"
})

annotations = annotations[[
    "rt_id",
    "review_theme",
    "review_observation"
]]

df = pd.merge(movies, reviews, on="rt_id", how="left")

df = pd.merge(df, annotations, on="rt_id", how="left")

df.to_csv("output/final_movie_dataset.csv", index=False)

print("Total movies:", len(df))
print("Reviews available:", df["review_text"].notna().sum())
print("Annotations:", df["review_theme"].notna().sum())

print(df[[
    "title",
    "audience_critic_gap",
    "review_theme",
    "review_observation"
]].head())

final = df.drop(columns=["review_text"])

final.to_csv("output/movie_reception_final.csv", index=False)

print("Final dataset:", len(final))
print("Missing review themes:", final["review_theme"].isna().sum())