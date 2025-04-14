from enum import Enum
from types import UnionType
from typing import Literal

LettersToA = Literal['a']
LettersToB = Literal['a', 'b']
LettersToC = Literal['a', 'b', 'c']
LettersToD = Literal['a', 'b', 'c', 'd']
LettersToE = Literal['a', 'b', 'c', 'd', 'e']
LettersToF = Literal['a', 'b', 'c', 'd', 'e', 'f']

RowNumber = Literal[1, 2, 3, 10, 11, 12, 13, 14, 15, 21, 24, 25, 26, 27, 32, 33, 34, 37, 38, 39, 40, 41, 42, 52, 53, 54]
ViableRowLetters: dict[RowNumber, UnionType] = {
    1: LettersToF,
    2: LettersToF,
    3: LettersToF,
    10: LettersToF,
    11: LettersToF,
    12: LettersToD,
    13: LettersToC,
    14: LettersToF,
    15: LettersToF,
    21: LettersToC,
    24: LettersToD,
    25: LettersToD,
    26: LettersToF,
    27: LettersToF,
    32: LettersToF,
    33: LettersToF,
    37: LettersToB,
    38: LettersToB,
    39: LettersToB,
    40: LettersToB,
    41: LettersToB,
    42: LettersToB,
    52: LettersToF,
    53: LettersToF,
    54: LettersToD
}

StartingGrade = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class ForeignLanguage(Enum):
    ENGLISH = 0
    FRENCH = 1
    SPANISH = 2

ClassLetter = Literal['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

class Subject(Enum):
    GERMAN = 0
    ENGLISH = 1
    FRENCH = 2
    LATIN = 3
    SPANISH = 4
    MUSIC = 5
    ART = 6
    THEATER = 7
    ENGLISH_Z = 8
    MUSIC_Z = 9
    
    POLITICS = 10
    HISTORY = 11
    GEOGRAPHY = 12
    PHILOSOPHY = 13
    
    MATHEMATICS = 14
    PHYSICS = 15
    CHEMISTRY = 16
    BIOLOGY = 17
    INFORMATICS = 18
    BIOLOGY_Z = 19
    
    PHYSICAL_EDUCATION = 20
    SKIING = 21
    SURFING = 22
    SUB = 23

class PPType(Enum):
    PP = 0
    BLL = 1
    bf = 2
    
