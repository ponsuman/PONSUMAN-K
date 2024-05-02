import pandas as pd

def test_dataset():
    data = pd.read_csv("../input/spotify-dataset/data/data.csv")
    genre_data = pd.read_csv('../input/spotify-dataset/data/data_by_genres.csv')
    year_data = pd.read_csv('../input/spotify-dataset/data/data_by_year.csv')
    print(data.info())
    print(genre_data.info())
    print(year_data.info())
