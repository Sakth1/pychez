try:
    from .ChessBoard import Board
    from .Pieces import Piece, Pawn, Bishop, Rook, Queen, King, Knight, MoveKind, MovePattern
except ImportError:
    from ChessBoard import Board
    from Pieces import Piece, Pawn, Bishop, Rook, Queen, King, Knight, MoveKind, MovePattern

class Chess:
    def __init__(self):
        self.board = Board()
        self.current_turn = "WHITE"
        self.check = False
        self.checkmate = False
        self.stalemate = False

    def InBounds(self, row: int, col: int) -> bool:
        return 1 <= row <= 8 and 1 <= col <= 8
    
    def IndexToPos(self, row: int, col: int) -> str:
        return self.board.files[col - 1] + self.board.ranks[row - 1]
    
    def IsEmpty(self, row: int, col: int) -> bool:
        return self.board.grid[row - 1][col - 1] is None
    
    def IsEnemy(self, row: int, col: int, color: str) -> bool:
        piece = self.board.grid[row - 1][col - 1]
        return piece is not None and piece.Color != color
    
    def IsAlly(self, row: int, col: int, color: str) -> bool:
        piece = self.board.grid[row - 1][col - 1]
        return piece is not None and piece.Color == color
    
    def RayMoves(self, row, col, directions, color):
        moves = []

        for direction_row, direction_col in directions:
            next_row = row + direction_row
            next_col = col + direction_col

            while self.InBounds(next_row, next_col) and self.IsEmpty(next_row, next_col):
                moves.append(self.IndexToPos(next_row, next_col))
                next_row += direction_row
                next_col += direction_col

            if self.InBounds(next_row, next_col) and self.IsEnemy(next_row, next_col, color):
                moves.append(self.IndexToPos(next_row, next_col))

        return moves

    def StepMoves(self, row, col, steps, color):
        moves = []

        for d_row, d_col in steps:
            next_row = row + d_row
            next_col = col + d_col

            if not self.InBounds(next_row, next_col):
                continue

            if self.IsEmpty(next_row, next_col) or self.IsEnemy(next_row, next_col, color):
                moves.append(self.IndexToPos(next_row, next_col))

        return moves

    def PawnMoves(self, row, col, pawn: Pawn):
        moves = []

        direction = -1 if pawn.Color == "WHITE" else 1
        start_row = 7 if pawn.Color == "WHITE" else 2

        one_step_row = row + direction

        # forward move
        if self.InBounds(one_step_row, col) and self.IsEmpty(one_step_row, col):
            moves.append(self.IndexToPos(one_step_row, col))

            # two-step on first move
            two_step_row = row + 2 * direction
            if row == start_row and self.IsEmpty(two_step_row, col):
                moves.append(self.IndexToPos(two_step_row, col))

        # diagonal captures
        for side_col in [col - 1, col + 1]:
            if self.InBounds(one_step_row, side_col) and \
            self.IsEnemy(one_step_row, side_col, pawn.Color):
                moves.append(self.IndexToPos(one_step_row, side_col))

        # TODO: en passant

        return moves
    
    def GenerateMoves(self, pos: str) -> list[str]:
        piece: Piece = self.board.GetPiece(pos)
        if piece is None:
            return []

        row, col = self.board._PosToIndex(pos)
        pattern = piece.MovementPattern()

        if pattern.Kind == MoveKind.RAY:
            return self.RayMoves(row, col, pattern.Directions, piece.Color)

        if pattern.Kind == MoveKind.STEP:
            return self.StepMoves(row, col, pattern.Directions, piece.Color)

        if pattern.Kind == MoveKind.PAWN:
            return self.PawnMoves(row, col, piece)

        return []
    
    def GenerateValidMoves(self):
        for row in range(1, 9):
            for col in range(1, 9):
                if self.IsAlly(row, col, self.current_turn):
                    piece = self.board.GetPiece(self.IndexToPos(row, col))
                    piece.ValidMoves = []
                    piece.ValidMoves.extend(self.GenerateMoves(self.IndexToPos(row, col)))
                    print('piece: ', piece, 'valid moves: ', piece.ValidMoves)

    def Start(self):
        self.board.SetupBoard()
        self.GenerateValidMoves()
        self.board.DisplayBoard()

    def switch_turn(self):
        self.current_turn = "BLACK" if self.current_turn == "WHITE" else "WHITE"

    def MovePiece(self, from_pos: str, to_pos: str):
        piece: Piece = self.board.GetPiece(from_pos)
        print(piece.ValidMoves)
        if piece is None:
            print("No piece at source square")
            return

        if piece.Color != self.current_turn:
            print("Not your turn")
            return

        move_successful = False
        print(f"Moving {type(piece)} from {from_pos} to {to_pos}")
        to_pos = to_pos[-2].upper() + to_pos[-1]

        if to_pos in piece.ValidMoves:
            self.board.MovePiece(from_pos, to_pos)
            move_successful = True

        if not move_successful:
            print("Invalid move")
            return

        self.switch_turn()
        self.board.DisplayBoard()
        self.GenerateValidMoves()
    

def main():
    chess = Chess()
    chess.Start()

    while True:
        from_pos = input("from: ")
        to_pos = input("to: ")
        chess.MovePiece(from_pos, to_pos)

if __name__ == "__main__":
    main()
