import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")

BASE_URL = "https://www.omdbapi.com/"


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
        print("Movie not found:", title)
        return None

    return data


if __name__ == "__main__":

    movie = get_movie("Inception")

    if movie:

        print("Title:", movie.get("Title"))
        print("Year:", movie.get("Year"))
        print("Genre:", movie.get("Genre"))
        print("Director:", movie.get("Director"))
        print("IMDb Rating:", movie.get("imdbRating"))