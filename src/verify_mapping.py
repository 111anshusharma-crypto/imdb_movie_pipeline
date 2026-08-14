import pandas as pd

mapping = pd.read_csv("data/mapping/movie_mapping.csv")
omdb = pd.read_csv("data/api/omdb_movies.csv")

merged = mapping.merge(
    omdb,
    on="imdb_id",
    how="left"
)

print(
    merged[
        ["title_x", "imdb_id", "title_y", "year", "genre", "imdb_rating"]
    ]
)