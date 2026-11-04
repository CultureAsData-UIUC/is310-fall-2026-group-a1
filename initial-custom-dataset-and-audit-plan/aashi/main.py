import os
import pandas as pd

rt = pd.read_csv("data/movie_info.csv")
lb = pd.read_parquet("data/train.parquet")

lb_avg = lb.groupby(["movie_id", "title"]).agg(
    letterboxd_rating=("rating", "mean"),
    rating_count=("rating", "count")
).reset_index()

rt["movie_key"] = rt["title"].str.lower()
rt["movie_key"] = rt["movie_key"].str.replace(
    r"[^a-z0-9]+", "-", regex=True
)
rt["movie_key"] = rt["movie_key"].str.strip("-")

lb_avg["movie_key"] = lb_avg["title"]

df = pd.merge(rt, lb_avg, on="movie_key", how="inner")

duplicates = df[df["movie_key"].duplicated(keep=False)]

rt = rt.drop_duplicates()

rt = rt[~rt["movie_key"].duplicated(keep=False)]
lb_avg = lb_avg[~lb_avg["movie_key"].duplicated(keep=False)]

df = pd.merge(rt, lb_avg, on="movie_key", how="inner")

df["critic_score"] = pd.to_numeric(
    df["critic_score"].str.replace("%", ""),
    errors="coerce"
)

df["audience_score"] = pd.to_numeric(
    df["audience_score"].str.replace("%", ""),
    errors="coerce"
)

df_clean = df.dropna(subset=["critic_score", "audience_score"]).copy()

df_clean = df_clean[df_clean["rating_count"] >= 25].copy()

df_clean["year"] = pd.to_numeric(
    df_clean["release_date"].str.extract(r"(\d{4})")[0],
    errors="coerce"
)

df_clean = df_clean[
    (df_clean["year"] >= 2015) &
    (df_clean["year"] <= 2024)
].copy()

df_clean["audience_critic_gap"] = (
    df_clean["audience_score"] - df_clean["critic_score"]
)

df_clean["reception_category"] = "Similar reception"

df_clean.loc[
    df_clean["audience_critic_gap"] >= 15,
    "reception_category"
] = "Audience-favored"

df_clean.loc[
    df_clean["audience_critic_gap"] <= -15,
    "reception_category"
] = "Critic-favored"

audience = df_clean[df_clean["reception_category"] == "Audience-favored"]
critics = df_clean[df_clean["reception_category"] == "Critic-favored"]
similar = df_clean[df_clean["reception_category"] == "Similar reception"]

audience = audience.sample(n=20, random_state=42)
critics = critics.sample(n=20, random_state=42)
similar = similar.sample(n=20, random_state=42)

movies = pd.concat([audience, critics, similar])

bad = ["deception", "run", "the-king"]

movies = movies[~movies["movie_key"].isin(bad)]

new = ["midsommar", "lady-bird", "hereditary"]

replacements = df_clean[df_clean["movie_key"].isin(new)]

movies = pd.concat([movies, replacements])

print("Final movies:", len(movies))
print(movies["reception_category"].value_counts())

movies = movies.rename(columns={"title_x": "title"})

movies = movies[[
    "title",
    "year",
    "critic_score",
    "audience_score",
    "audience_critic_gap",
    "letterboxd_rating",
    "rating_count",
    "reception_category",
    "url",
    "movie_id",
    "title_y"
]]

movies = movies.sort_values("title")

movies.to_csv("output/movie_sample_60.csv", index=False)

check = movies[[
    "title",
    "year",
    "title_y",
    "movie_id",
    "url"
]]

check.to_csv("output/check_matches.csv", index=False)

movies["gap_reasoning"] = ""
movies["review_url"] = ""
movies["review_sentiment"] = ""
movies["review_theme"] = ""
movies["review_observation"] = ""
movies["annotation_status"] = "Pending"

if not os.path.exists("output/movie_annotations.csv"):
    movies.to_csv("output/movie_annotations.csv", index=False)

annotations = pd.read_csv("output/movie_annotations.csv")

annotations["gap_reasoning"] = annotations["gap_reasoning"].astype("string")

for i in annotations.index:
    gap = annotations.loc[i, "audience_critic_gap"]

    if gap >= 15:
        reasoning = f"The audience score is {int(gap)} percentage points higher than the critic score, showing more positive audience reception."

    elif gap <= -15:
        reasoning = f"The critic score is {int(abs(gap))} percentage points higher than the audience score, showing more positive critical reception."

    else:
        reasoning = f"The critic and audience scores differ by only {int(abs(gap))} percentage points, suggesting similar reception."

    annotations.loc[i, "gap_reasoning"] = reasoning

annotations.to_csv("output/movie_annotations.csv", index=False)

reviews = pd.read_csv(
    "data/rotten_tomatoes_movie_reviews.csv",
    nrows=5
)

movies["rt_id"] = movies["url"].str.split("/m/").str[-1]

movies["review_id"] = movies["rt_id"]

movies.loc[
    movies["title"] == "Game Night",
    "review_id"
] = "game_night_2018"

matched_reviews = []

for chunk in pd.read_csv(
    "data/rotten_tomatoes_movie_reviews.csv",
    chunksize=50000
):
    matches = chunk[chunk["id"].isin(movies["review_id"])]
    matched_reviews.append(matches)

reviews = pd.concat(matched_reviews, ignore_index=True)

reviews = reviews.dropna(subset=["reviewText", "reviewUrl"])

reviews = reviews[reviews["reviewText"].str.len() >= 100].copy()

reviews["review_length"] = reviews["reviewText"].str.len()

reviews = reviews.sort_values("review_length", ascending=False)
selected = reviews.drop_duplicates(subset=["id"])

selected = selected[[
    "id",
    "reviewText",
    "scoreSentiment",
    "reviewUrl",
    "criticName"
]]

review_data = pd.merge(
    movies[["title", "rt_id"]],
    selected,
    left_on="rt_id",
    right_on="id",
    how="left"
)

review_data.to_csv("output/selected_reviews.csv", index=False)

print("Movies with usable reviews:", review_data["reviewText"].notna().sum())

missing = review_data[review_data["reviewText"].isna()]

missing_ids = missing["rt_id"].tolist()

possible_matches = set()

for chunk in pd.read_csv(
    "data/rotten_tomatoes_movie_reviews.csv",
    usecols=["id"],
    chunksize=50000
):
    for movie_id in missing_ids:
        matches = chunk[
            chunk["id"].str.contains(movie_id, regex=False, na=False)
        ]

        possible_matches.update(matches["id"].tolist())

print("\nPossible review matches:")
print(sorted(possible_matches))

