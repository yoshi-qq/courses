from types import UnionType
from typing import Union, Literal

def getLetters(amount: int) -> UnionType:
    letters = [Literal['a'], Literal['b'], Literal['c'], Literal['d'], Literal['e'], Literal['f']]
    return Union[letters[0:amount]]



RowNumber = Union[]
viableRowNumbers: list[int] = [1, 2, 3, 10, 11, 12, 13, 14, 15, 21, 24, 25, 26, 27, 32, 33, 34, 37, 38, 39, 40, 41, 42, 52, 53, 54]
viableRowLetters = {
    1: getLetters(6),
    2: getLetters(6),
    3: getLetters(6),
    10: getLetters(6),
    11: getLetters(6),
    12: getLetters(4),
    13: getLetters(3),
    14: getLetters(6),
    15: getLetters(6),
    21: getLetters(3),
    24: getLetters(4),
    25: getLetters(4),
    26: getLetters(6),
    27: getLetters(6),
    32: getLetters(6),
    33: getLetters(6),
    37: getLetters(2),
    38: getLetters(2),
    39: getLetters(2),
    40: getLetters(2),
    41: getLetters(2),
    42: getLetters(2),
    52: getLetters(6),
    53: getLetters(6),
    54: getLetters(4)
}