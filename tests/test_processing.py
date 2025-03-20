# import pytest
import sys
sys.path.append('../src')
from data_processing import convert_column_to_list

# Example test case: testing the clean_data function
# def test_clean_data():
#     # Sample input for the clean_data function (you should use actual inputs)
#     input_data = {
#         'title': ['Movie 1', 'Movie 2'],
#         'budget': [100, None],
#         'revenue': [200, 150],
#     }
    
#     output_data = clean_data(input_data)  # Assume clean_data removes rows with missing values

#     assert len(output_data) == 2  # Assert that after cleaning, there are no missing values

# # Example test case: testing the preprocess_genres function
def test_preprocess_genres():
    genres = 'Action|Adventure|Comedy'
    processed_genres = convert_column_to_list(genres)  # Assume it splits the genres into a list

    assert isinstance(processed_genres, list)
    assert 'Action' in processed_genres
    assert 'Comedy' in processed_genres