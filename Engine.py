from itertools import cycle

from ChessBoard import Board
from Pieces import Pawn

class Chess:
    Turn = cycle(("WHITE", "BLACK"))

    def __init__(self):
        self.board = Board()
        self.current_turn = "WHITE"
        self.check = False
        self.can_en_passant = False
        self.checkmate = False
        self.stalemate = False

    def Start(self):
        self.board.SetupBoard()
        self.board.DisplayBoard()

    def switch_turn(self):
        self.current_turn = next(self.Turn)

    def MovePiece(self, from_pos: str, to_pos: str):
        #piece_type = self.board.GetPiece(to_pos, True)
        piece = self.board.GetPiece(from_pos)
        piece_color = piece.color
        if type(piece) == Pawn:
            if self.MovePawn(from_pos, to_pos, piece):
                pass

        self.switch_turn()
        self.board.DisplayBoard()

    def MovePawn(self, from_pos: str, to_pos: str, pawn: Pawn):
        validation_info: dict = pawn.IsMovementValid(from_pos, to_pos)
        if not validation_info.get("Valid"):
            print("invalid movement")
            return False
        
        if from_pos[-2] != to_pos[-2]: #pawn moved to a different file
            if self.board.GetPiece(to_pos, return_type=True) == str: #there is a piece at end position
                if self.can_en_passant:
                    print("en passant")
                    if self.can_en_passant:
                        self.can_en_passant = False
                    
                    self.can_en_passant = validation_info.get("en_passant")
                    self.board.MovePiece(from_pos, to_pos)
                    en_passant_pos = to_pos[-2] + str(int(to_pos[-1]) + (pawn.MovementDirection * -1))
                    print(en_passant_pos)
                    self.board.SetPiece(en_passant_pos, ".")
                    return True
                
                else:
                    print("There is a piece in the way")
                    return False

        pos_in_front = from_pos[0] + str(int(from_pos[1]) + pawn.MovementDirection)
        if self.board.GetPiece(pos_in_front, return_type=True) != str: #there is a piece infront of pawn
            print("there is a piece infront of pawn")
            return False

        if self.can_en_passant:
            self.can_en_passant = False
        
        self.can_en_passant = validation_info.get("en_passant")
        self.board.MovePiece(from_pos, to_pos)
        
        pawn.HasMoved = True
        

            
