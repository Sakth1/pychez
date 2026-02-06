from typing import Any, List, Literal
from dataclasses import dataclass

@dataclass
class Pawn(object):
    def __init__(self, color: str):
        self.color = color
        self.HasMoved = False
        self._setup_attributes_()

    def _setup_attributes_(self):
        self.notation = "P" if self.color.upper() in ["W", "WHITE"] else "p" if self.color.upper() in ["B", "BLACK"] else None
        self.MovementDirection = 1 if self.color.upper() in ["W", "WHITE"] else -1

    def __repr__(self) -> str:
        return self.notation
    
    def _get_moving_direction_(self, from_pos: list, to_pos: list):
        start_idx = from_pos[-1]
        end_idx = to_pos[-1]
        return 1 if start_idx < end_idx else -1
        
    def IsMovementValid(self, from_pos: list, to_pos: list) -> bool:
        if not self._get_moving_direction_(from_pos, to_pos) == self.MovementDirection:
            print("invalid direction")
            return {"Valid": False, "en_passant": False}
        
        if abs(int(from_pos[-1]) - int(to_pos[-1])) > 1:
            if self.HasMoved:
                return {"Valid": False, "en_passant": False}
            else:
                return {"Valid": True, "en_passant": True}
        
        return {"Valid": True, "en_passant": False}
    
@dataclass
class King(object):
    def __init__(self, color: str):
        self.color = color
        self.HasMoved = False
        self._setup_attributes_()

    def _setup_attributes_(self):
        self.notation = "K" if self.color.upper() in ["W", "WHITE"] else "k" if self.color.upper() in ["B", "BLACK"] else None

    def __repr__(self) -> str:
        return self.notation
        
@dataclass
class Queen(object):
    def __init__(self, color: str):
        self.color = color
        self._setup_attributes_()

    def _setup_attributes_(self):
        self.notation = "Q" if self.color.upper() in ["W", "WHITE"] else "q" if self.color.upper() in ["B", "BLACK"] else None

    def __repr__(self) -> str:
        return self.notation
        
@dataclass
class Rook(object):
    def __init__(self, color: str):
        self.color = color
        self.HasMoved = False
        self._setup_attributes_()

    def _setup_attributes_(self):
        self.notation = "R" if self.color.upper() in ["W", "WHITE"] else "r" if self.color.upper() in ["B", "BLACK"] else None

    def __repr__(self) -> str:
        return self.notation
        
@dataclass
class Knight(object):
    def __init__(self, color: str):
        self.color = color
        self._setup_attributes_()

    def _setup_attributes_(self):
        self.notation = "N" if self.color.upper() in ["W", "WHITE"] else "n" if self.color.upper() in ["B", "BLACK"] else None

    def __repr__(self) -> str:
        return self.notation
        
@dataclass
class Bisshop(object):
    def __init__(self, color: str):
        self.color = color
        self._setup_attributes_()

    def _setup_attributes_(self):
        self.notation = "B" if self.color.upper() in ["W", "WHITE"] else "b" if self.color.upper() in ["B", "BLACK"] else None

    def __repr__(self) -> str:
        return self.notation

    