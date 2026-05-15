import re
from models import Book
from storage import Storage
from stats import Stats


def main():
    storage = Storage("books.json")

    while True:
        print("\n" + "=" * 40)
        print("    ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
        print("=" * 40)
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        print("=" * 40)

        choice = input("Выберите действие (1-6): ").strip()

        if choice == "1":
            add_book(storage)
        elif choice == "2":
            show_all_books(storage)
        elif choice == "3":
            Stats.print_average_rating(storage.get_all_books())
        elif choice == "4":
            Stats.print_author_stats(storage.get_all_books())
        elif choice == "5":
            delete_book(storage)
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз.")


def add_book(storage: Storage):
    print("\n--- Добавление книги ---")

    title = input("Название: ").strip()
    if not title:
        print("Название не может быть пустым.")
        return

    author = input("Автор: ").strip()
    if not author:
        print("Автор не может быть пустым.")
        return

    while True:
        rating_input = input("Оценка (1-5): ").strip()
        if rating_input.isdigit() and 1 <= int(rating_input) <= 5:
            rating = int(rating_input)
            break
        print("Введите целое число от 1 до 5.")

    while True:
        date_read = input("Дата прочтения (ГГГГ-ММ-ДД): ").strip()
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date_read):
            break
        print("Введите дату в формате ГГГГ-ММ-ДД (например, 2024-05-15).")

    book = Book(title=title, author=author, rating=rating, date_read=date_read)
    if storage.add_book(book):
        print(f"Книга '{title}' успешно добавлена.")
    else:
        print(f"Книга '{title}' этого автора уже есть в библиотеке.")


def show_all_books(storage: Storage):
    books = storage.get_all_books()
    if not books:
        print("\nБиблиотека пока пуста.")
        return
    print(f"\nВсего книг: {len(books)}")
    for i, book in enumerate(books, 1):
        print(f"  {i}. {book}")


def delete_book(storage: Storage):
    title = input("\nНазвание книги для удаления: ").strip()
    if not title:
        print("Название не может быть пустым.")
        return
    if storage.delete_book(title):
        print(f"Книга '{title}' удалена.")
    else:
        print("Книга не найдена.")


if __name__ == "__main__":
    main()
