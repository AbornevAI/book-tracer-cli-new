import json
from typing import List
from models import Book


class Storage:
    def __init__(self, filename: str = "books.json"):
        self.filename = filename
        self.books: List[Book] = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.books = [Book.from_dict(b) for b in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []
            self.save_books()

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self, book: Book) -> bool:
        if any(b.title.lower() == book.title.lower() and
               b.author.lower() == book.author.lower()
               for b in self.books):
            return False
        self.books.append(book)
        self.save_books()
        return True

    def get_all_books(self) -> List[Book]:
        return self.books.copy()

    def delete_book(self, title: str) -> bool:
        before = len(self.books)
        self.books = [b for b in self.books if b.title.lower() != title.lower()]
        if len(self.books) < before:
            self.save_books()
            return True
        return False
