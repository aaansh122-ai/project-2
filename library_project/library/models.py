from abc import ABC, abstractmethod
from typing import Optional

class Book(ABC):
    def __init__(self, isbn: str, title: str, author: str, copies: int = 1):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__copies = copies

    @property
    def isbn(self): return self.__isbn
    @property
    def title(self): return self.__title
    @property
    def author(self): return self.__author
    @property
    def copies(self): return self.__copies

    def add_copies(self, n=1): self.__copies += n
    def remove_copy(self):
        if self.__copies <= 0: raise ValueError("No copies available")
        self.__copies -= 1
    def return_copy(self): self.__copies += 1

    @abstractmethod
    def calculate_late_fee(self, days_late: int) -> float: pass


class PrintedBook(Book):
    def calculate_late_fee(self, days_late: int) -> float:
        return round(0.5 * max(0, days_late), 2)


class EBook(Book):
    def calculate_late_fee(self, days_late: int) -> float:
        return round(0.2 * max(0, days_late), 2)
