import pandas as pd
from typing import List, Any

from Pieces import Pawn, Bisshop, Rook, Queen, King, Knight

class Board(object):

    def __init__(self):
        self.columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.index = ["8", "7", "6", "5", "4", "3", "2", "1"]
        self.board = pd.DataFrame(data=[["."] * 8 for _ in range(8)], dtype=object, index=self.index, columns=self.columns)
        self.SetupBoard()

    def SetupBoard(self):
        #pawn setup
        self.board.loc["2", :] = [Pawn("WHITE") for _ in range(8)]
        self.board.loc["7", :] = [Pawn("BLACK") for _ in range(8)]
        #self.board.loc["3", "E"] = Pawn("w")
        
        #Rook setup
        self.board.loc["1", "A"] = Rook("WHITE")
        self.board.loc["1", "H"] = Rook("WHITE")
        self.board.loc["8", "A"] = Rook("BLACK")
        self.board.loc["8", "H"] = Rook("BLACK")

        #Knight setup
        self.board.loc["1", "B"] = Knight("WHITE")
        self.board.loc["1", "G"] = Knight("WHITE")
        self.board.loc["8", "B"] = Knight("BLACK")
        self.board.loc["8", "G"] = Knight("BLACK")

        #Bishop setup
        self.board.loc["1", "C"] = Bisshop("WHITE")
        self.board.loc["1", "F"] = Bisshop("WHITE")
        self.board.loc["8", "C"] = Bisshop("BLACK")
        self.board.loc["8", "F"] = Bisshop("BLACK")

        #Queen setup
        self.board.loc["1", "D"] = Queen("WHITE")
        self.board.loc["8", "D"] = Queen("BLACK")

        #King setup
        self.board.loc["1", "E"] = King("WHITE")
        self.board.loc["8", "E"] = King("BLACK")

    def DisplayBoard(self):
        print('\n', self.board, '\n')

    def GetPiece(self, pos: str, return_type: bool = False) -> Any:
        print('pos:', pos)
        if return_type:
            return type(self.board.loc[str(pos[-1]), str(pos[-2].capitalize())])
        return self.board.loc[pos[-1], pos[-2].capitalize()]

    def SetPiece(self, pos: str, piece: Any):
        self.board.loc[pos[-1], pos[-2].capitalize()] = piece
        
    def MovePiece(self, from_pos: str, to_pos: str):
        starting_rank = from_pos[-1]
        starting_file = from_pos[-2].capitalize()
        piece = self.board.loc[starting_rank, starting_file]

        self.board.loc[starting_rank, starting_file] = "."
        self.board.loc[to_pos[-1], to_pos[-2].capitalize()] = piece

        print(self.board)