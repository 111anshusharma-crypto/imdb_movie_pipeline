import pandas as pd

mapping = pd.read_csv("data/mapping/movie_mapping.csv")
omdb = pd.read_csv("data/api/omdb_movies.csv")

# Remove title from mapping because OMDb already has the movie title
mapping = mapping[["imdb_id"]]

# Merge using IMDb ID
final_df = mapping.merge(
    omdb,
    on="imdb_id",
    how="left"
)

# Select required columns
final_df = final_df[
    [
        "title",
        "year",
        "genre",
        "director",
        "actors",
        "imdb_rating",
        "imdb_id"
    ]
]

# Save final dataset
final_df.to_csv(
    "data/final/movie_metadata.csv",
    index=False
)

print("Final dataset created successfully!")
print("Rows:", len(final_df))
print("Columns:", final_df.columns.tolist())
print()
print(final_df.head())