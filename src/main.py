from loader import load_imdb_dataset
from cleaner import clean_dataset
from sampler import stratified_sample, show_distribution


RAW_PATH = "data/raw/IMDB_Dataset.csv"
SAMPLE_PATH = "data/sampled/imdb_stratified.csv"


def main():

    # Step 1: Load dataset
    df = load_imdb_dataset(RAW_PATH)

    print("\nBefore cleaning:")
    print("Rows:", len(df))

    # Step 2: Clean dataset
    df = clean_dataset(df)

    print("\nAfter cleaning:")
    print("Rows:", len(df))

    # Step 3: Show original sentiment distribution
    print("\nOriginal distribution:")
    show_distribution(df)

    # Step 4: Stratified sampling
    sampled_df = stratified_sample(
        df,
        sample_size=10000
    )

    # Step 5: Show sampled distribution
    print("\nSampled distribution:")
    show_distribution(sampled_df)

    # Step 6: Save sampled dataset
    sampled_df.to_csv(
        SAMPLE_PATH,
        index=False
    )

    print(
        f"\nSample saved successfully to: {SAMPLE_PATH}"
    )


if __name__ == "__main__":
    main()