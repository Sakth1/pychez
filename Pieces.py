from typing import Any, List, Literal
from dataclasses import dataclass

@dataclass
class Pawn(object):
    def __init__(self, color: str):
        self.color = color
        self.HasMoved = False
        self._setup_attributes_()

    def _setup_attributes_(self):
        self.notation = "P" if self.color.lower() in ["w", "white"] else "p"
        self.MovementDirection = 1 if self.color.lower() in ["w", "white"] else -1

    def __repr__(self) -> str:
        return self.notation
    
    def _get_moving_direction_(self, from_pos: list, to_pos: list):
        start_idx = from_pos[-1]
        end_idx = to_pos[-1]
        return 1 if start_idx < end_idx else -1
        
    def IsMovementValid(self, from_pos: list, to_pos: list) -> bool:
        if not self._get_moving_direction_(from_pos, to_pos) == self.MovementDirection:
            print("invalid  direction")
            return False
        
        if abs(int(from_pos[-1]) - int(to_pos[-1])) > 1 and self.HasMoved:
            return False            
        
        return True
    
@dataclass
class King(object):
    def __init__(self, color: str):
        self.color = color
        self.HasMoved = False

    def __repr__(self) -> str:
        if self.color.lower() in ["w", "white"]:
            return "K"
        else:
            return "k"
        
@dataclass
class Queen(object):
    def __init__(self, color: str):
        self.color = color

    def __repr__(self) -> str:
        if self.color.lower() in ["w", "white"]:
            return "Q"
        else:
            return "q"
        
@dataclass
class Rook(object):
    def __init__(self, color: str):
        self.color = color
        self.HasMoved = False

    def __repr__(self) -> str:
        if self.color.lower() in ["w", "white"]:
            return "R"
        else:
            return "r"
        
@dataclass
class Knight(object):
    def __init__(self, color: str):
        self.color = color

    def __repr__(self) -> str:
        if self.color.lower() in ["w", "white"]:
            return "K"
        else:
            return "k"
        
@dataclass
class Bisshop(object):
    def __init__(self, color: str):
        self.color = color

    def __repr__(self) -> str:
        if self.color.lower() in ["w", "white"]:
            return "B"
        else:
            return "b"


    