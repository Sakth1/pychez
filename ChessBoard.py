import pandas as pd

class Board(pd.DataFrame):

    def __init__(self):
        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        index = ["1", "2", "3", "4", "5", "6", "7", "8"]
        super().__init__(data=[["."] * 8 for _ in range(8)], index=index, columns=columns)

        print(self)
