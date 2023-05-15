import pandas as pd
from  day04.ex01 import YoungestFellah
from day04.ex00.FileLoader import FileLoader



def proportion_by_sport(df:pd.DataFrame, year:int, sport:str, genr:str):
    if not (isinstance(df, pd.DataFrame) and isinstance(year, int) and
    isinstance(sport, str) and genr in ['F', 'M']):
        return None

    filtered_yr_gr = (df["Year"] == year) & (df["Sex"] == genr)
    filtered_sport =  (df["Sport"] == sport)

    return  (filtered_sport.shape[0] / filtered_yr_gr.shape[0])

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../../resources/athlete_events.csv')

    print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
