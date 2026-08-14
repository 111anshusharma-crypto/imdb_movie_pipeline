import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "https://www.omdbapi.com/"


MOVIE_TITLES = [
    "Inception",
    "The Dark Knight",
    "Titanic",
    "Avatar",
    "Interstellar",
    "The Matrix",
    "Forrest Gump",
    "Gladiator",
    "The Godfather",
    "Jurassic Park"
]


def get_movie(title):

    params = {
        "apikey": API_KEY,
        "t": title,
        "plot": "short",
        "r": "json"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    if data.get("Response") == "False":
        print(f"Movie not found: {title}")
        return None

    return data


def pull_movies(titles):

    movies = []

    for title in titles:

        print(f"Fetching: {title}")

        movie = get_movie(title)

        if movie:
            movies.append({
                "title": movie.get("Title"),
                "year": movie.get("Year"),
                "genre": movie.get("Genre"),
                "director": movie.get("Director"),
                "actors": movie.get("Actors"),
                "imdb_rating": movie.get("imdbRating"),
                "imdb_id": movie.get("imdbID")
            })

        # Small delay between requests
        time.sleep(0.5)

    return movies


def main():

    if not API_KEY:
        raise ValueError(
            "OMDB_API_KEY not found in .env"
        )

    movies = pull_movies(MOVIE_TITLES)

    df = pd.DataFrame(movies)

    os.makedirs("data/api", exist_ok=True)

    output_path = "data/api/omdb_movies.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("\nAPI pull completed!")
    print("Movies collected:", len(df))
    print("Saved to:", output_path)

    print("\nCollected data:")
    print(df)


if __name__ == "__main__":
    main()