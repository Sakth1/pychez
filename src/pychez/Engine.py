from .ChessBoard import Board
from .Pieces import Piece, Pawn, Bishop, Rook, Queen, King, Knight

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
        if piece is None:
            print("No piece at source square")
            return

        if piece.Color != self.current_turn:
            print("Not your turn")
            return

        move_successful = False
        print(f"Moving {type(piece)} from {from_pos} to {to_pos}")
        if isinstance(piece, Pawn):
            move_successful = self.MovePawn(from_pos, to_pos, piece)
        elif isinstance(piece, Rook):
            move_successful = self.MoveRook(from_pos, to_pos, piece)
        elif isinstance(piece, Knight):
            move_successful = self.MoveKnight(from_pos, to_pos, piece)
        elif isinstance(piece, Bishop):
            move_successful = self.MoveBishop(from_pos, to_pos, piece)
        elif isinstance(piece, Queen):
            move_successful = self.MoveQueen(from_pos, to_pos, piece)
        elif isinstance(piece, King):
            move_successful = self.MoveKing(from_pos, to_pos, piece)
        else:
            print("Invalid piece")
            return

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
            if self.board.GetPiece(to_pos) == None: #there is a piece at end position
                if self.can_en_passant:
                    self.board.MovePiece(from_pos, to_pos)
                    en_passant_pos = to_pos[-2] + str(int(to_pos[-1]) + (pawn.MovementDirection * -1))
                    self.board.SetPiece(en_passant_pos, ".")
                    return True
                
                else:
                    print("Cannot move to a different file")
                    return False

        pos_in_front = from_pos[0] + str(int(from_pos[1]) + pawn.MovementDirection)
        if self.board.GetPiece(pos_in_front) != None: #there is a piece infront of pawn
            print("there is a piece infront of pawn")
            return False
        
        self.can_en_passant = validation_info.get("EnPassant")
        self.board.MovePiece(from_pos, to_pos)
        
        pawn.HasMoved = True
        return True

    def MoveRook(self, from_pos: str, to_pos: str, rook: Rook):
        pass

    def MoveKnight(self, from_pos: str, to_pos: str, knight: Knight):
        pass

    def MoveBishop(self, from_pos: str, to_pos: str, bishop: Bishop):
        pass

    def MoveQueen(self, from_pos: str, to_pos: str, queen: Queen):
        pass

    def MoveKing(self, from_pos: str, to_pos: str, king: King):
        pass

    def BuildValidMoveList(self, piece: Piece):
        movement_pattern = piece.MovementPattern()
    

def main():
    chess = Chess()
    chess.Start()

    while True:
        from_pos = input("from: ")
        to_pos = input("to: ")
        chess.MovePiece(from_pos, to_pos)

if __name__ == "__main__":
    main()
