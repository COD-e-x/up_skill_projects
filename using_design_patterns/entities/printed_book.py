class PrintedBook:
    """Книга библиотеки."""

    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.available = True
