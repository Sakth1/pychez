

from ChessBoard import Board

class Game:
    def __init__(self):
        self.board = Board
        self.turn = "white"
        self.check = False
        self.checkmate = False
        self.stalemate = False
        