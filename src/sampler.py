from sklearn.model_selection import train_test_split


def stratified_sample(df, sample_size=10000):

    if sample_size > len(df):
        raise ValueError(
            "Sample size cannot be greater than dataset size"
        )

    sampled_df, _ = train_test_split(
        df,
        train_size=sample_size,
        stratify=df["sentiment"],
        random_state=42
    )

    return sampled_df.reset_index(drop=True)


def show_distribution(df):

    print("\nSentiment distribution:")
    print(df["sentiment"].value_counts())

    print("\nPercentage distribution:")
    print(
        df["sentiment"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )