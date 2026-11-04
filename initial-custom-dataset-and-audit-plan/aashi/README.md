## Movie Popularity acoss Critics and Audiences

### Research Question

How does movie reception differ across critics and audiences, and across different platforms (Rotten Tomatoes and Letterboxd)?

### Dataset

I have made a dataset with 60 different movies that were released sometime between 2015 and 2024. I got ratings for Letterboxd and Rotten Tomatoes from public datasets, and got a dataset for the Rotten Tomatoes critic reviews. 

- [Rotten Tomatoes ratings](https://data.mendeley.com/datasets/kbpvrwfp5z/1)
- [Letterboxd ratings](https://huggingface.co/datasets/titouann/letterboxd-10m-movies-ratings-2025)
- [Rotten Tomatoes critic reviews](https://huggingface.co/datasets/haoxianc/andrezaza_clapper-massive-rotten-tomatoes-movies-and-reviews)

### Method

I used Python (pandas library) to clean the dataset, then join Letterboxd and Rotten Tomatoes ratings by movie title. I removed duplicates, removed data with missing ratings, and kept movies from only 2015-2024, which had at least 25 Letterboxd ratings. I also manually checked that the movies matched exactly, and corrected 3 incorrect matches.

I also calculates the audience to critic gap - audience score - critic score, and then classified based on the results, into audience favored (gap >= 15), critic favored (<= -15), and similar reception (gap between -14 and 14).

I then randomly picked 20 movies from each category using a random state of 42 to make the results reproducible.

### Annotations

I matched the movies to an existing dataset on critic reviews and picked one review per movie randomly, as long as the minimum length was above 100 characters. I then reviewed them and identified the themes I found in the reviews, and wrote some observations. I found reviews for 53 movies, the left over 7 have missing review information.

### Limitations and Findings

The original datasets that I used for the data entry portion had some missing values, duplicate titles, and some wrong matches as well with the python script. Rotten tomatoes looks at the number of positive ratings, and Letterboxd looks at star ratings, and the Letterboxd average comes from just a sample of users not the whole platform.

My sample is useful because you can compare reception categories but it does not represent the whole distribution of movie opinions. Also, one singular review cannot represent every critic's perception.

The dataset can show how movies receive different levels of approval from critics versus audiences, and written reviews can also add context to the numerical scores.

### Files

- main.py - cleans, joins, classifies the movie ratings
- merge_all.py - combines the ratings, reviews, annotations
- output/movie_reception_final.csv - final dataset
- audit_plan.md - plan to expand the dataset in the future

The raw data that was used will be linked rather than uploaded to Github.
