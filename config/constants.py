from types import UnionType
from typing import Union, Literal

lettersToA = Literal['a']
lettersToB = Literal['a', 'b']
lettersToC = Literal['a', 'b', 'c']
lettersToD = Literal['a', 'b', 'c', 'd']
lettersToE = Literal['a', 'b', 'c', 'd', 'e']
lettersToF = Literal['a', 'b', 'c', 'd', 'e', 'f']



RowNumber = Union[]
viableRowNumbers: list[int] = [1, 2, 3, 10, 11, 12, 13, 14, 15, 21, 24, 25, 26, 27, 32, 33, 34, 37, 38, 39, 40, 41, 42, 52, 53, 54]
viableRowLetters = {
    1: lettersToF,
    2: lettersToF,
    3: lettersToF,
    10: lettersToF,
    11: lettersToF,
    12: lettersToD,
    13: lettersToC,
    14: lettersToF,
    15: lettersToF,
    21: lettersToC,
    24: lettersToD,
    25: lettersToD,
    26: lettersToF,
    27: lettersToF,
    32: lettersToF,
    33: lettersToF,
    37: lettersToB,
    38: lettersToB,
    39: lettersToB,
    40: lettersToB,
    41: lettersToB,
    42: lettersToB,
    52: lettersToF,
    53: lettersToF,
    54: lettersToD
}