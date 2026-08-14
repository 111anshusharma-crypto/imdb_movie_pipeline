# IMDb Movie Data Pipeline

## Data Sources

1. IMDb Movie Review Dataset from Kaggle
   - Contains movie reviews and sentiment labels.
   - Columns: review, sentiment

2. OMDb Live API
   - Provides movie metadata.
   - Fields include title, year, genre, director,
     actors, IMDb rating and IMDb ID.

## Processing

1. Load raw IMDb dataset
2. Clean reviews
3. Apply stratified sampling
4. Pull live movie metadata from OMDb
5. Store API results separately
6. Join datasets only when a reliable movie
   title or IMDb ID is available

## Important Data Integrity Rule

OMDb metadata must not be randomly assigned
to IMDb reviews. A reliable movie identifier
is required for a valid join.