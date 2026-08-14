import pandas as pd


IMDB_PATH = "data/sampled/imdb_stratified.csv"
OMDB_PATH = "data/api/omdb_movies.csv"


def validate_imdb(df):

    print("\n--- IMDb Dataset Validation ---")

    print("Rows:", len(df))
    print("Columns:", list(df.columns))

    # Missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Duplicate reviews
    print("\nDuplicate reviews:", df["review"].duplicated().sum())

    # Sentiment distribution
    print("\nSentiment distribution:")
    print(df["sentiment"].value_counts())

    # Check sample size
    if len(df) == 10000:
        print("\n✓ Sample size is correct")
    else:
        print("\n✗ Sample size is not 10,000")

    # Check balance
    counts = df["sentiment"].value_counts()

    if (
        counts.get("positive", 0) == 5000
        and counts.get("negative", 0) == 5000
    ):
        print("✓ Stratified distribution is correct")
    else:
        print("✗ Sentiment distribution needs checking")


def validate_omdb(df):

    print("\n--- OMDb Dataset Validation ---")

    print("Rows:", len(df))
    print("Columns:", list(df.columns))

    print("\nMissing values:")
    print(df.isnull().sum())

    print(
        "\nDuplicate IMDb IDs:",
        df["imdb_id"].duplicated().sum()
    )

    print("\nMovie data:")
    print(df[["title", "year", "imdb_id"]])


def main():

    imdb_df = pd.read_csv(IMDB_PATH)
    omdb_df = pd.read_csv(OMDB_PATH)

    validate_imdb(imdb_df)
    validate_omdb(omdb_df)

    print("\n==============================")
    print("DATA VALIDATION COMPLETED")
    print("==============================")


if __name__ == "__main__":
    main()