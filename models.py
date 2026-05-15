class Book:
    def __init__(self, title: str, author: str, rating: int, date_read: str):
        self.title = title.strip()
        self.author = author.strip()
        self.rating = max(1, min(5, int(rating)))
        self.date_read = date_read.strip()

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "rating": self.rating,
            "date_read": self.date_read,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data.get("title", ""),
            author=data.get("author", ""),
            rating=data.get("rating", 1),
            date_read=data.get("date_read", ""),
        )

    def __str__(self):
        return f'"{self.title}" — {self.author} ({self.date_read}, оценка: {self.rating}/5)'
