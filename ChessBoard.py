import pandas as pd
from typing import List

from Pieces import Pawn, Bisshop, Rook, Queen, King, Knight

class Board(object):

    def __init__(self):
        self.columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.index = ["8", "7", "6", "5", "4", "3", "2", "1"]
        self.board = pd.DataFrame(data=[["."] * 8 for _ in range(8)], dtype=object, index=self.index, columns=self.columns)
        self.SetupBoard()

    def SetupBoard(self):
        #pawn setup
        self.board.loc["2", :] = [Pawn("white") for _ in range(8)]
        self.board.loc["7", :] = [Pawn("black") for _ in range(8)]
        
        #Rook setup
        self.board.loc["1", "A"] = Rook("white")
        self.board.loc["1", "H"] = Rook("white")
        self.board.loc["8", "A"] = Rook("black")
        self.board.loc["8", "H"] = Rook("black")

        #Knight setup
        self.board.loc["1", "B"] = Knight("white")
        self.board.loc["1", "G"] = Knight("white")
        self.board.loc["8", "B"] = Knight("black")
        self.board.loc["8", "G"] = Knight("black")

        #Bishop setup
        self.board.loc["1", "C"] = Bisshop("white")
        self.board.loc["1", "F"] = Bisshop("white")
        self.board.loc["8", "C"] = Bisshop("black")
        self.board.loc["8", "F"] = Bisshop("black")

        #Queen setup
        self.board.loc["1", "D"] = Queen("white")
        self.board.loc["8", "D"] = Queen("black")

        #King setup
        self.board.loc["1", "E"] = King("white")
        self.board.loc["8", "E"] = King("black")

        print(type(self.board.loc["1", "E"]))

    def GetPositionInfo(self, position: str):
        rank = position[-1]
        file = position[-2].capitalize()
        piece = self.board.loc[rank, file]
        return {"from_pos": [rank, file], "piece": piece}

    def MovePiece(self, from_pos: str, to_pos: str):
        CurrentPositionInfo = self.GetPositionInfo(from_pos)
        MovingPositionInfo = self.GetPositionInfo(to_pos)

        if CurrentPositionInfo["piece"].Move(CurrentPositionInfo["from_pos"], MovingPositionInfo["from_pos"]):
            self.board.loc[MovingPositionInfo["from_pos"][0], MovingPositionInfo["from_pos"][1]] = CurrentPositionInfo["piece"]
            self.board.loc[CurrentPositionInfo["from_pos"][0], CurrentPositionInfo["from_pos"][1]] = "."

        print(self.board)        