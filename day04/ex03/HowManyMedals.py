import pandas as pd
from  day04.ex01 import YoungestFellah
from day04.ex00.FileLoader import FileLoader

def how_many_medals(df:pd.DataFrame, name:str):
    if not (isinstance(df, pd.DataFrame) and isinstance(name, str)):
        return None
    filtered_name = df[ df["Name"] == name]
    res = dict()
    for _, row in filtered_name.iterrows():
        yr = row["Year"]
        medal = row["Medal"]
        if  yr not in res.keys():
            res.update({yr: {"G": 0, "S": 0, "B": 0}})
        if medal == "Gold":
            res[yr]["G"] += 1
        elif medal == "Silver":
            res[yr]["S"] += 1
        elif medal == "Bronze":
            res[yr]["B"] += 1        
    return res

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../../resources/athlete_events.csv')

    print(how_many_medals(data, 'Kjetil Andr Aamodt'))
