from dataclasses import dataclass, field
from typing import Literal, Any, Tuple, Optional, List
from enum import Enum, auto


COLOR = Literal["WHITE", "BLACK"]
DIRECTIONS = Tuple[int, int]


class MoveKind(Enum):
    RAY = auto()     # keep going until blocked (rook, bishop, queen)
    STEP = auto()    # single jumps (king, knight)
    PAWN = auto()    # special pawn logic


@dataclass
class MovePattern:
    Kind: MoveKind
    Directions: Optional[List[DIRECTIONS]] = None


def NormalizeColor(color: str) -> COLOR:
    c = color.strip().upper()
    if c in ("W", "WHITE"):
        return "WHITE"
    if c in ("B", "BLACK"):
        return "BLACK"
    raise ValueError(f"Invalid color: {color}")


@dataclass
class BasePiece:
    Color: COLOR
    HasMoved: bool = field(default=False, init=False)
    Notation: str = field(init=False)
    CurrentPosition: str = field(init=False)
    ValidMoves: list = field(init=False)

    def __post_init__(self):
        self.Color = NormalizeColor(self.Color)
        self.Notation = self._BuildNotation()

    def _BuildNotation(self) -> str:
        letter = self.BaseLetter()
        return letter.upper() if self.Color == "WHITE" else letter.lower()

    def __repr__(self) -> str:
        return self.Notation
    
    def BaseLetter(self) -> str:
        raise NotImplementedError

    def MovementPattern(self) -> MovePattern:
        raise NotImplementedError
    
    def GetValidMoves(self) -> list:
        raise self.ValidMoves
    

class Pawn(BasePiece):

    def BaseLetter(self) -> str:
        return "p"

    @property
    def MovementDirection(self) -> int:
        return 1 if self.Color == "WHITE" else -1
    
    def MovementPattern(self) -> MovePattern:
        return MovePattern(MoveKind.PAWN)

    def _GetCurrentMovingDirection(self, FromPos: tuple, ToPos: tuple) -> int:
        return 1 if FromPos[-1] < ToPos[-1] else -1


class Rook(BasePiece):
    def BaseLetter(self) -> str:
        return "r"
    
    def MovementPattern(self) -> MovePattern:
        return MovePattern(
            MoveKind.RAY,
            Directions=[
                (1, 0),   # up
                (-1, 0),  # down
                (0, 1),   # right
                (0, -1)   # left
            ]
        )
    

class King(BasePiece):
    def BaseLetter(self) -> str:
        return "k"
    
    def MovementPattern(self) -> MovePattern:
        return MovePattern(
            MoveKind.RAY,
            Directions=[
                (1, 0),   # up
                (-1, 0),  # down
                (0, 1),   # right
                (0, -1),  # left
                (1, 1),   # up-right
                (1, -1),  # up-left
                (-1, 1),  # down-right
                (-1, -1)  # down-left
            ]
        )


class Queen(BasePiece):
    def BaseLetter(self) -> str:
        return "q"
    
    def MovementPattern(self) -> MovePattern:
        return MovePattern(
            MoveKind.RAY,
            Directions=[
                (1, 0),   # up
                (-1, 0),  # down
                (0, 1),   # right
                (0, -1),  # left
                (1, 1),   # up-right
                (1, -1),  # up-left
                (-1, 1),  # down-right
                (-1, -1)  # down-left
            ]
        )


class Knight(BasePiece):
    def BaseLetter(self) -> str:
        return "n"
    
    def MovementPattern(self) -> MovePattern:
        return MovePattern(
            MoveKind.STEP,
            Directions=[
                (2, 1),    # up-right
                (2, -1),   # up-left
                (-2, 1),   # down-right
                (-2, -1),  # down-left
                (1, 2),    # right-up
                (1, -2),   # right-down
                (-1, 2),   # left-up
                (-1, -2),  # left-down
            ]
        )


class Bishop(BasePiece):
    def BaseLetter(self) -> str:
        return "b"
    
    def MovementPattern(self) -> MovePattern:
        return MovePattern(
            MoveKind.RAY,
            Directions=[
                (1, 1),    # up-right
                (1, -1),   # up-left
                (-1, 1),   # down-right
                (-1, -1)   # down-left
            ]
        )

