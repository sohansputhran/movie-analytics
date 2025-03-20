"""

This script reads the raw data, cleans it, and saves the cleaned data to a new CSV file.

"""

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def handling_outliers(df, column):
    # Calculate Q1, Q3, and IQR for the 'revenue_musd' column
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    # Define outlier thresholds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    # print(f"Number of outliers in {column}: {outliers.shape[0]}")

    # Capping outliers
    df[column] = np.where(df[column] > upper_bound, upper_bound,
                    np.where(df[column] < lower_bound, lower_bound,
                        df[column]))
    return df

# Convert columns with "|" into a list
def convert_column_to_list(df, column):
    return df[column].str.split('|').tolist()

def main():
    # Reading the movies data
    movies_df = pd.read_csv("data/raw/movies_complete.csv")

    # Convert release_date to datetime
    movies_df['release_date'] = pd.to_datetime(movies_df['release_date'])

    # Extract year from release_date
    movies_df['release_year'] = movies_df['release_date'].dt.year

    # Handling outliers in 'revenue_musd'
    movies_df = handling_outliers(movies_df, 'revenue_musd')

    # Handling outliers in 'budget_musd'
    movies_df = handling_outliers(movies_df, 'budget_musd')

    # Handling outliers in 'popularity'
    movies_df = handling_outliers(movies_df, 'popularity')

    # Handling outliers in 'vote_count'
    movies_df = handling_outliers(movies_df, 'vote_count')

    # Handling outliers in 'vote_average'
    movies_df = handling_outliers(movies_df, 'vote_average')

    # Handling outliers in 'runtime'
    movies_df = handling_outliers(movies_df, 'runtime')

    # Split genres into individual genres (if not already done)
    movies_df['genres'] = movies_df['genres'].fillna('')  # Handling NaN values
    genres_split = movies_df['genres'].str.split('|', expand=True)
    # Flatten the list of genres and create a set to get unique genres
    all_genres = set(genres_split.values.flatten())
    all_genres.remove(None)
    all_genres.remove('')
    # Create a column for each genre with binary values
    for genre in all_genres:
        movies_df[genre] = movies_df['genres'].apply(lambda x: 1 if genre in x else 0)

    # Convert columns with "|" into a list
    movies_df['production_companies'] = convert_column_to_list(movies_df, 'production_companies')
    movies_df['spoken_languages'] = convert_column_to_list(movies_df, 'spoken_languages')
    movies_df['cast'] = convert_column_to_list(movies_df, 'cast')
    movies_df['genres'] = convert_column_to_list(movies_df, 'genres')

    # Save the cleaned data to a new CSV file
    movies_df.to_csv("data/processed/movies_cleaned.csv", index=False)
    print("Data cleaning and preprocessing completed.")

if __name__ == "__main__":
    main()
