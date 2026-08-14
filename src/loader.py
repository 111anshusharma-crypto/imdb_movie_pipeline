import pandas as pd


def load_imdb_dataset(path):
    df = pd.read_csv(path)

    print("Dataset loaded successfully!")
    print("Number of rows:", len(df))
    print("Columns:", list(df.columns))

    return df


if __name__ == "__main__":

    df = load_imdb_dataset(
        "data/raw/IMDB_Dataset.csv"
    )

    print("\nFirst 5 rows:")
    print(df.head())