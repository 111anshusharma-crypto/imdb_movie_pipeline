import pandas as pd

df = pd.read_csv("data/final/movie_metadata.csv")

movie_name = input("Enter movie name: ").strip().lower()

result = df[df["title"].str.lower().str.contains(movie_name, na=False)]

if result.empty:
    print("\n❌ Movie not found.")
else:
    print("\n🎬 Movie Found:\n")

    for _, movie in result.iterrows():
        print("Title:", movie["title"])
        print("Year:", movie["year"])
        print("Genre:", movie["genre"])
        print("Director:", movie["director"])
        print("Actors:", movie["actors"])
        print("IMDb Rating:", movie["imdb_rating"])
        print("IMDb ID:", movie["imdb_id"])
        print("-" * 50)