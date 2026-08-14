import os
import pandas as pd

print("=== IMDb Movie Pipeline Validation ===")
print()

# 1. Stratified dataset
sample_path = "data/sampled/imdb_stratified.csv"

if os.path.exists(sample_path):
    df = pd.read_csv(sample_path)
    print("✅ Stratified dataset found")
    print("   Rows:", len(df))
    print("   Columns:", df.columns.tolist())
    print("   Sentiment distribution:")
    print(df["sentiment"].value_counts().to_string())
else:
    print("❌ Stratified dataset not found")

print()

# 2. OMDb dataset
omdb_path = "data/api/omdb_movies.csv"

if os.path.exists(omdb_path):
    omdb = pd.read_csv(omdb_path)
    print("✅ OMDb dataset found")
    print("   Rows:", len(omdb))
    print("   Columns:", omdb.columns.tolist())
else:
    print("❌ OMDb dataset not found")

print()

# 3. Final dataset
final_path = "data/final/movie_metadata.csv"

if os.path.exists(final_path):
    final = pd.read_csv(final_path)
    print("✅ Final movie metadata found")
    print("   Rows:", len(final))
    print("   Columns:", final.columns.tolist())
else:
    print("❌ Final dataset not found")

print()
print("=== Validation Complete ===")