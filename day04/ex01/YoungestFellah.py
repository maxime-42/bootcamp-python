import pandas as pd
from FileLoader import FileLoader

def youngest_fellah(df:pd.DataFrame, year:int):


    if not (isinstance(df, pd.DataFrame) and isinstance(year, int)):
        return { 'F': NaN, 'M': NaN }

    filt_f = (df["Year"] == year) & (df["Sex"] == "F")
    filtered_df = df[filt_f]  # Apply the filter
    min_age_f = filtered_df["Age"].min()  # Get the minimum age from the filtered DataFrame

    filt_m = (df["Year"] == year) & (df["Sex"] == "M")
    filtered_dm = df[filt_m]  # Apply the filter
    min_age_m = filtered_dm["Age"].min()  # Get the minimum age from the filtered DataFrame    
    return {
        "f" : min_age_f,
        "m":  min_age_m,
    }





if __name__ == "__main__":
    test = FileLoader()
    data = test.load("athlete_events.csv")

    print(youngest_fellah(data, 1992)) # {'F': 12.0, 'M': 11.0}
    print(youngest_fellah(data, 2004)) # {'F': 13.0, 'M': 14.0}
    print(youngest_fellah(data, 2010)) # {'F': 15.0, 'M': 15.0}

