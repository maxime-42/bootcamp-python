import pandas as pd
import sys

class FileLoader:
    def __init_(self):
        pass
    def load(self, path:str):
        try:
            self.df = pd.read_csv(path)
        except Exception as error_msg:
            print(error_msg, file=sys.stderr)
            sys.exit()
        else:
            num_rows, num_columns = self.df.shape
            print(f"The dataset has {num_rows} rows and {num_columns} columns.")
            return self.df

    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        else:
            n *= -1
            print(df.tail(n))

if __name__=="__main__":
    test = FileLoader()
    df = test.load("athlete_events.csv")
    test.display(df, -10)
