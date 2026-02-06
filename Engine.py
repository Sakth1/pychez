from ChessBoard import Board
from Pieces import Piece, Pawn

class Chess:
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
        self.current_turn = "BLACK" if self.current_turn == "WHITE" else "WHITE"

    def MovePiece(self, from_pos: str, to_pos: str):
        piece: Piece = self.board.GetPiece(from_pos)

        if piece.Color != self.current_turn:
            print("Not your turn")
            return

        move_successful = False
        if type(piece) == Pawn:
            move_successful = self.MovePawn(from_pos, to_pos, piece)

        if not move_successful:
            return

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

                    self.board.MovePiece(from_pos, to_pos)
                    en_passant_pos = to_pos[-2] + str(int(to_pos[-1]) + (pawn.MovementDirection * -1))
                    self.board.SetPiece(en_passant_pos, ".")
                    return True
                
                else:
                    print("Cannot move to a different file")
                    return False

        pos_in_front = from_pos[0] + str(int(from_pos[1]) + pawn.MovementDirection)
        if self.board.GetPiece(pos_in_front, return_type=True) != str: #there is a piece infront of pawn
            print("there is a piece infront of pawn")
            return False
        
        self.can_en_passant = validation_info.get("EnPassant")
        self.board.MovePiece(from_pos, to_pos)
        
        pawn.HasMoved = True
        return True


            
