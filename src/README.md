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