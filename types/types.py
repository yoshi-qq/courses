from typing import Literal, Optional
from config.constants import RowNumber, LettersToF, ForeignLanguage, StartingGrade, ClassLetter, Subject, PPType

class Course:
    def __init__(self, subject: Subject, PP: Optional[PPType], examSubject: Literal[1, 2, 3, 4], mandatoryCourses: Optional[Literal[1, 2, 3, 4]], semesters: tuple[bool, bool, bool, bool], weekPeriods: int, creditAmount: int) -> None:
        self.subject = subject
        self.PP = PP
        self.examSubject = examSubject
        self.mandatoryCourses = mandatoryCourses
        self.semesters = semesters
        self.weekPeriods = weekPeriods
        self.creditAmount = creditAmount

class OverviewSheet:
    def __init__(self, name: str, surname: str, row: tuple[RowNumber, LettersToF], foreignLanguages: list[tuple[ForeignLanguage, StartingGrade]], entryyear: int, classLetter: ClassLetter, courses: list[Course]) -> None:
        self.name = name
        self.surname = surname
        self.row = row
        self.foreignLanguages = foreignLanguages
        self.entryyear = entryyear
        self.classLetter = classLetter
        self.courses = courses