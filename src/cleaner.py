import re


def clean_text(text):
    # Convert to string
    text = str(text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove spaces from beginning and end
    return text.strip()


def clean_dataset(df):

    # Make a copy so original DataFrame is not changed
    df = df.copy()

    # Remove rows where review or sentiment is missing
    df = df.dropna(
        subset=["review", "sentiment"]
    )

    # Remove duplicate reviews
    df = df.drop_duplicates(
        subset=["review"]
    )

    # Clean review text
    df["review"] = df["review"].apply(
        clean_text
    )

    return df