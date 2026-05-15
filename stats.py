from collections import Counter
from typing import List
from models import Book


class Stats:
    @staticmethod
    def average_rating(books: List[Book]) -> float:
        if not books:
            return 0.0
        return round(sum(b.rating for b in books) / len(books), 2)

    @staticmethod
    def books_by_author(books: List[Book]) -> dict:
        return dict(Counter(b.author for b in books))

    @staticmethod
    def print_average_rating(books: List[Book]):
        if not books:
            print("Библиотека пока пуста.")
            return
        print(f"\nСредняя оценка: {Stats.average_rating(books)} / 5")

    @staticmethod
    def print_author_stats(books: List[Book]):
        if not books:
            print("Библиотека пока пуста.")
            return
        print("\nСтатистика по авторам:")
        for author, count in sorted(Stats.books_by_author(books).items(),
                                    key=lambda x: x[1], reverse=True):
            print(f"  {author}: {count} кн.")
