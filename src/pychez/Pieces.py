from dataclasses import dataclass, field
from typing import Literal, Any


COLOR = Literal["WHITE", "BLACK"]


def NormalizeColor(color: str) -> COLOR:
    c = color.strip().upper()
    if c in ("W", "WHITE"):
        return "WHITE"
    if c in ("B", "BLACK"):
        return "BLACK"
    raise ValueError(f"Invalid color: {color}")


@dataclass
class Piece:
    Color: COLOR
    HasMoved: bool = field(default=False, init=False)
    Notation: str = field(init=False)
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
    
    def IsMovementValid(self, FromPos: tuple, ToPos: tuple) -> Any:
        raise NotImplementedError

    def MovementPattern(self):
        raise NotImplementedError
    
    def GetValidMoves(self) -> list:
        raise self.ValidMoves
    

class Pawn(Piece):

    def BaseLetter(self) -> str:
        return "p"

    @property
    def MovementDirection(self) -> int:
        return 1 if self.Color == "WHITE" else -1

    def _GetCurrentMovingDirection(self, FromPos: tuple, ToPos: tuple) -> int:
        return 1 if FromPos[-1] < ToPos[-1] else -1
    
    def MovementPattern(self):
        pass

    def IsMovementValid(self, FromPos: tuple, ToPos: tuple) -> dict:
        if self._GetCurrentMovingDirection(FromPos, ToPos) != self.MovementDirection:
            return {"Valid": False, "EnPassant": False}

        distance = abs(int(FromPos[-1]) - int(ToPos[-1]))

        if distance > 1:
            if self.HasMoved:
                return {"Valid": False, "EnPassant": False}
            return {"Valid": True, "EnPassant": True}

        return {"Valid": True, "EnPassant": False}



class Rook(Piece):
    def BaseLetter(self) -> str:
        return "r"
    
    def IsMovementValid(self, FromPos: tuple, ToPos: tuple) -> dict:
        #change_in_rank_and_file = FromPos[-1] == ToPos[-1] and FromPos[-2] != ToPos[-2]
        #if () or (FromPos[-2] == ToPos[-2] and FromPos[-1] != ToPos[-1]):
        pass

class King(Piece):
    def BaseLetter(self) -> str:
        return "k"


class Queen(Piece):
    def BaseLetter(self) -> str:
        return "q"


class Knight(Piece):
    def BaseLetter(self) -> str:
        return "n"


class Bishop(Piece):
    def BaseLetter(self) -> str:
        return "b"
