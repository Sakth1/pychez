import pandas as pd
from typing import List

from Pieces import Pawn

class Board(object):

    def __init__(self):
        self.columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.index = ["8", "7", "6", "5", "4", "3", "2", "1"]
        self.board = pd.DataFrame(data=[["."] * 8 for _ in range(8)], dtype=object, index=self.index, columns=self.columns)
        self.SetupBoard()

    def SetupBoard(self):
        self.board.loc["2", :] = [Pawn("white") for _ in range(8)]
        self.board.loc["7", :] = [Pawn("black") for _ in range(8)]
        print(self.board)