from using_design_patterns.factories.dase_book_factory import BookFactory
from using_design_patterns.entities.printed_book import PrintedBook


class PrintedBookFactory(BookFactory):
    """Фабрика для печатных книг."""

    def create_book(self, book_id, title, genre, year):
        return PrintedBook(book_id, title, genre, year)
