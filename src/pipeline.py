import pandas as pd
import os

from loader import load_imdb_dataset
from cleaner import clean_dataset
from sampler import stratified_sample, show_distribution


RAW_PATH = "data/raw/IMDB_Dataset.csv"
SAMPLE_PATH = "data/sampled/imdb_stratified.csv"


def main():

    print("=" * 50)
    print("IMDb MOVIE DATA PIPELINE")
    print("=" * 50)

    # 1. Load raw dataset
    print("\n[1] Loading IMDb dataset...")

    df = load_imdb_dataset(RAW_PATH)

    print("Raw rows:", len(df))

    # 2. Clean dataset
    print("\n[2] Cleaning dataset...")

    df = clean_dataset(df)

    print("Clean rows:", len(df))

    # 3. Show distribution
    print("\n[3] Original sentiment distribution:")

    show_distribution(df)

    # 4. Stratified sampling
    print("\n[4] Applying stratified sampling...")

    sampled_df = stratified_sample(
        df,
        sample_size=10000
    )

    # 5. Show sampled distribution
    print("\n[5] Sampled distribution:")

    show_distribution(sampled_df)

    # 6. Create output folder
    os.makedirs("data/sampled", exist_ok=True)

    # 7. Save sample
    sampled_df.to_csv(
        SAMPLE_PATH,
        index=False
    )

    print("\n[6] Sample saved successfully!")
    print("Location:", SAMPLE_PATH)

    print("\nFinal sample shape:")
    print(sampled_df.shape)

    print("\nPipeline completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()