# MovieAnalytics

Movie Analytics is a data science project aimed at exploring and analyzing a comprehensive movie dataset. The project includes various analyses such as movie success prediction, genre popularity, director and cast performance, and the correlation between budget, revenue, and runtime. Using machine learning, data visualization, and natural language processing (NLP), this repository provides valuable insights into the film industry. The goal is to uncover patterns and relationships that influence movie success, while also demonstrating various data science techniques applied to real-world movie data.

__Some additional information on Features/Columns__:

* **id:** The ID of the movie (clear/unique identifier).
* **title:** The Official Title of the movie.
* **tagline:** The tagline of the movie.
* **release_date:** Theatrical Release Date of the movie.
* **genres:** Genres associated with the movie.
* **belongs_to_collection:** Gives information on the movie series/franchise the particular film belongs to.
* **original_language:** The language in which the movie was originally shot in.
* **budget_musd:** The budget of the movie in million dollars.
* **revenue_musd:** The total revenue of the movie in million dollars.
* **production_companies:** Production companies involved with the making of the movie.
* **production_countries:** Countries where the movie was shot/produced in.
* **vote_count:** The number of votes by users, as counted by TMDB.
* **vote_average:** The average rating of the movie.
* **popularity:** The Popularity Score assigned by TMDB.
* **runtime:** The runtime of the movie in minutes.
* **overview:** A brief blurb of the movie.
* **spoken_languages:** Spoken languages in the film.
* **poster_path:** The URL of the poster image.
* **cast:** (Main) Actors appearing in the movie.
* **cast_size:** number of Actors appearing in the movie.
* **director:** Director of the movie.
* **crew_size:** Size of the film crew (incl. director, excl. actors).


This repository contains a data science project to analyze a movie dataset. It includes exploratory data analysis (EDA), machine learning models to predict movie success, and data visualizations. The goal is to uncover insights into the film industry.

## Setup
- Clone the repository.
- Install dependencies: `pip install -r requirements.txt`.
- Run Jupyter notebooks in the `notebooks/` directory.

## Workflow
- Code is tested automatically on push to `main` via GitHub Actions.
