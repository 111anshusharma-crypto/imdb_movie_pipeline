import pandas as pd
import os


IMDB_PATH = "data/sampled/imdb_stratified.csv"
OMDB_PATH = "data/api/omdb_movies.csv"
OUTPUT_PATH = "data/final/final_dataset.csv"


def main():

    # Load IMDb sampled dataset
    imdb_df = pd.read_csv(IMDB_PATH)

    # Load OMDb API dataset
    omdb_df = pd.read_csv(OMDB_PATH)

    print("IMDb dataset:")
    print(imdb_df.shape)

    print("\nOMDb dataset:")
    print(omdb_df.shape)

    # Create final folder
    os.makedirs("data/final", exist_ok=True)

    # Save both datasets as separate sections/files
    imdb_df.to_csv(
        "data/final/imdb_reviews.csv",
        index=False
    )

    omdb_df.to_csv(
        "data/final/omdb_metadata.csv",
        index=False
    )

    print("\nFinal datasets saved successfully!")

    print("\nIMDb reviews:")
    print(imdb_df.head())

    print("\nOMDb metadata:")
    print(omdb_df.head())


if __name__ == "__main__":
    main()