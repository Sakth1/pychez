from Pieces import Piece, Pawn, Bishop, Rook, Queen, King, Knight

def CellNotation(cell) -> str:
    match cell:
        case None:
            return "."
        case Piece():
            return cell.Notation

class Board:

    def __init__(self):
        self.files = ["A","B","C","D","E","F","G","H"]
        self.ranks = ["8","7","6","5","4","3","2","1"]

        self.grid: list[list[Piece | None]] = [
            [None for _ in range(8)] for _ in range(8)
        ]

        self.SetupBoard()

    def _PosToIndex(self, pos: str) -> tuple[int, int]:
        file = pos[0].upper()
        rank = pos[1]

        row = self.ranks.index(rank)
        col = self.files.index(file)

        return row, col

    def SetupBoard(self):
        for f in self.files:
            self.SetPiece(f + "2", Pawn("WHITE"))
            self.SetPiece(f + "7", Pawn("BLACK"))

        self.SetPiece("A1", Rook("WHITE"))
        self.SetPiece("H1", Rook("WHITE"))
        self.SetPiece("A8", Rook("BLACK"))
        self.SetPiece("H8", Rook("BLACK"))

        self.SetPiece("B1", Knight("WHITE"))
        self.SetPiece("G1", Knight("WHITE"))
        self.SetPiece("B8", Knight("BLACK"))
        self.SetPiece("G8", Knight("BLACK"))

        self.SetPiece("C1", Bishop("WHITE"))
        self.SetPiece("F1", Bishop("WHITE"))
        self.SetPiece("C8", Bishop("BLACK"))
        self.SetPiece("F8", Bishop("BLACK"))

        self.SetPiece("D1", Queen("WHITE"))
        self.SetPiece("D8", Queen("BLACK"))

        self.SetPiece("E1", King("WHITE"))
        self.SetPiece("E8", King("BLACK"))

    def GetPiece(self, pos: str) -> Piece | None:
        r, c = self._PosToIndex(pos)
        return self.grid[r][c]

    def SetPiece(self, pos: str, piece: Piece | None):
        r, c = self._PosToIndex(pos)
        self.grid[r][c] = piece

    def MovePiece(self, from_pos: str, to_pos: str):
        piece = self.GetPiece(from_pos)
        self.SetPiece(from_pos, None)
        self.SetPiece(to_pos, piece)

    def DisplayBoard(self):
        print()
        for r in range(8):
            row = [CellNotation(self.grid[r][c]) for c in range(8)]
            print(self.ranks[r], "  ", " ".join(row))
        print('\n    ', " ".join(self.files), '\n')
