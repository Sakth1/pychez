from typing import Any, List, Literal
from dataclasses import dataclass

@dataclass
class Pawn(object):
    def __init__(self, color: str):
        self.color = color

    def __repr__(self) -> str:
        if self.color.lower() in ["w", "white"]:
            return "P"
        else:
            return "p"
        
@dataclass
class King(object):
    def __init__(self, color: str):
        self.color = color

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


    