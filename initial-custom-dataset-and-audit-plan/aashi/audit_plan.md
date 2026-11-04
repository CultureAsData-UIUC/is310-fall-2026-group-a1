## Movie Reception - Audit & Next Steps

### Goal

I want to see how movie reception can be different between critics and audiences, and can a single rating represent how people feel about a movie.

### Expansion Plan

I want to use the audit and augment existing data approach, by combining my 60 movie dataset with larger datasets - Rotten Tomatoes, Letterboxd, and maybe IMDb.

I will use Python and pandas to match the movies, handle any missing values, and also compare ratings and movie rankings as well across platforms. 

### What I want to study

- Do critics and audiences normally agree about movies?
- Do Rotten Tomatoes and Letterboxd audiences usually favor the same movies?
- What do numerical ratings normally leave out about someone's opinions?

Because the platforms all calculate ratings differently, I will als look at movie rankings rather than only looking at star ratings and percentages.

### Challenges and Limitations

One of the errors I ran into was that title and release date may not be in the exact same format, so matching movies across datasets can cause some mistakes. Sometimes, ratings are also missing, and each platform has different rating methods.

Scaling up will make it very hard to manually check the movies or reviews, I am thinking about automating matching and review classification, then manually verifying sample of the results and documenting any errors.

### Final Goal

I want to show how different rating systems can represent the same movie differently, and why popularity cannot always be explained by a single number.