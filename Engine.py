

from ChessBoard import Board
from Pieces import Pawn

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.check = False
        self.checkmate = False
        self.stalemate = False

    def Start(self):
        self.board.SetupBoard()
        self.board.DisplayBoard()

    def MovePiece(self, from_pos: str, to_pos: str):
        #piece_type = self.board.GetPiece(to_pos, True)
        piece = self.board.GetPiece(from_pos)
        if type(piece) == Pawn:
            self.MovePawn(from_pos, to_pos, piece)

        self.board.DisplayBoard()

    def MovePawn(self, from_pos: str, to_pos: str, pawn: Pawn):
        if not pawn.IsMovementValid(from_pos, to_pos):
            print("invalid movement")
            return False
        
        if self.board.GetPiece(from_pos, return_type=True) == str: #there is a piece infront of pawn
            print("there is a piece infront of pawn")
            return False

        self.board.MovePiece(from_pos, to_pos)
        
        pawn.HasMoved = True
        

            
