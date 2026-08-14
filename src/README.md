# IMDb Movie Data Pipeline

## Project Overview

This project builds a data pipeline using the IMDb movie review dataset and the OMDb live API.

## Pipeline

Raw IMDb Dataset
→ Data Cleaning
→ Stratified Sampling
→ OMDb API Pull
→ Data Validation

## Data Sources

### IMDb Dataset
Contains:
- review
- sentiment

### OMDb API
Provides:
- Title
- Year
- Genre
- Director
- Actors
- IMDb Rating
- IMDb ID

## Stratified Sampling

A sample of 10,000 reviews is created while maintaining the sentiment distribution:

- Positive: 5,000
- Negative: 5,000

## Technologies

- Python
- Pandas
- Requests
- Scikit-learn
- python-dotenv
- OMDb API

## Project Structure

```text
imdb_movie_pipeline/
├── data/
├── src/
├── .env
├── .gitignore
├── README.md
└── venv/

## Results

The pipeline successfully:

- Loaded the IMDb movie review dataset.
- Cleaned the review data.
- Applied stratified sampling.
- Created a balanced sample of 10,000 reviews.
- Pulled live movie metadata from the OMDb API.
- Stored API results in CSV format.
- Performed data quality validation.
- Uploaded the project to GitHub.

## Sample Dataset

The stratified sample contains:

| Sentiment | Count |
|-----------|------:|
| Positive  | 5,000 |
| Negative  | 5,000 |
| Total     | 10,000 |

## OMDb API Data

The API pull collects:

- Movie title
- Release year
- Genre
- Director
- Actors
- IMDb rating
- IMDb ID

## Data Quality

Validation checks include:

- Missing values
- Duplicate reviews
- Sentiment distribution
- Sample size
- Duplicate IMDb IDs

## Project Architecture

```text
Kaggle IMDb Dataset
        |
        v
   Data Loading
        |
        v
   Data Cleaning
        |
        v
Stratified Sampling
        |
        v
  10,000 Reviews
        |
        +----------------+
        |                |
        v                v
   IMDb Dataset      OMDb API
                         |
                         v
                  Movie Metadata
                         |
                         v
                    CSV Storage
                         |
                         v
                   Validation

**⌘ + S** दबाकर save करो.

---

### Step 20.2 — GitHub par changes push karo

VS Code Terminal mein:

```bash
git add README.md