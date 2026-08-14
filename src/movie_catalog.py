import pandas as pd


OMDB_PATH = "data/api/omdb_movies.csv"
OUTPUT_PATH = "data/final/movie_catalog.csv"


def main():

    df = pd.read_csv(OMDB_PATH)

    # Keep useful movie identification columns
    catalog = df[
        [
            "title",
            "year",
            "genre",
            "director",
            "actors",
            "imdb_rating",
            "imdb_id"
        ]
    ].copy()

    # Remove duplicate IMDb IDs
    catalog = catalog.drop_duplicates(
        subset=["imdb_id"]
    )

    catalog.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print("Movie catalog created successfully!")
    print("Movies:", len(catalog))
    print("\nColumns:")
    print(catalog.columns.tolist())

    print("\nMovie catalog:")
    print(catalog)


if __name__ == "__main__":
    main()