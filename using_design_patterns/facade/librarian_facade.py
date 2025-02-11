from using_design_patterns.entities.librarian import Librarian
from using_design_patterns.strategys.search_by_title import SearchByTitle
from using_design_patterns.strategys.search_by_author import SearchByAuthor
from using_design_patterns.strategys.search_by_year import SearchByYear


class LibrarianFacade:
    def __init__(self, librarian: Librarian):
        """Фасад для упрощенного управления библиотекой."""

        self.librarian = librarian

    def subscribe(self, event_type, listener):
        """Подписывает слушателя на событие."""
        self.librarian.subscribe(event_type, listener)

    def unsubscribe(self, event_type, listener):
        """Отписывает слушателя от события."""
        self.librarian.unsubscribe(event_type, listener)

    def add_book(self, book_id, title, author, year):
        """Добавляет книгу в библиотеку."""
        self.librarian.add_book(book_id, title, author, year)

    def remove_book(self, book_id):
        """Удаляет книгу из библиотеки."""
        self.librarian.remove_book(book_id)

    def update_book(self, book_id, new_book_id, new_title, new_author, new_year):
        """Обновляет информацию о книге."""
        self.librarian.update_book(book_id, new_book_id, new_title, new_author, new_year)

    def add_reader(self, reader_id, name, email):
        """Добавляет читателя в библиотеку."""
        self.librarian.add_reader(reader_id, name, email)

    def remove_reader(self, reader_id):
        """Удаляет читателя из библиотеки."""
        self.librarian.remove_reader(reader_id)

    def update_reader(self, reader_id, new_reader_id, new_name, new_email):
        """Обновляет информацию о читателе."""
        self.librarian.update_reader(reader_id, new_reader_id, new_name, new_email)

    def borrow_book(self, reader_name, book_title):
        """Выдает книгу читателю."""
        return self.librarian.borrow_book(reader_name, book_title)

    def return_book(self, reader_name, book_title):
        """Принимает возвращенную книгу."""
        return self.librarian.return_book(reader_name, book_title)

    def search_books_by_title(self, title):
        """Ищет книги по названию."""
        self.librarian.set_search_strategy(SearchByTitle())
        return self.librarian.search_books(title)

    def search_books_by_author(self, author):
        """Ищет книги по автору."""
        self.librarian.set_search_strategy(SearchByAuthor())
        return self.librarian.search_books(author)

    def search_books_by_year(self, year):
        """Ищет книги по году издания."""
        self.librarian.set_search_strategy(SearchByYear())
        return self.librarian.search_books(year)
