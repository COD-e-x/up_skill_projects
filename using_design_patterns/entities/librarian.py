from using_design_patterns.utils.json_utils import write_json
from using_design_patterns.utils.find_entity_id import find_entity_id
from using_design_patterns.factories.dase_book_factory import BookFactory
from using_design_patterns.factories.base_reader_factory import ReaderFactory
from using_design_patterns.managers.event_manager import EventManager


class Librarian:
    """Класс библиотекаря, управляющий книгами и читателями."""

    def __init__(self, book: BookFactory, reader: ReaderFactory, event_manager: EventManager):
        self.book = book
        self.reader = reader
        self.event_manager = event_manager
        self.search_strategy = None
        self.path = './data/books.json'
        self.library_database = {'books': {}, 'readers': {}, 'borrowed_book': {}}

    def subscribe(self, event_type, listener):
        """Подписывает слушателя на событие."""
        self.event_manager.subscribe(event_type, listener)

    def unsubscribe(self, event_type, listener):
        """Отписывает слушателя от события."""
        self.event_manager.unsubscribe(event_type, listener)

    def add_book(self, book_id, title, author, year):
        """Добавляет книгу в базу данных."""
        create_book = self.book.create_book(book_id, title, author, year)
        self.library_database['books'][book_id] = create_book.__dict__
        write_json(self.path, self.library_database)
        self.event_manager.notify('add_book', f'Книга добавлена: {title}')

    def remove_book(self, book_id):
        """Удаляет книгу из базы данных."""
        if book_id in self.library_database['books']:
            data = self.library_database['books'].pop(book_id)
            write_json(self.path, self.library_database)
            self.event_manager.notify('remove_book', f'Книга удалена: {data}')
        else:
            self.event_manager.notify('remove_book',
                                      f'Попытка удалить книгу по ID{book_id}: не найдена в базе.')

    def update_book(self, book_id, new_book_id, new_title, new_author, new_year):
        """Обновляет данные книги."""
        if book_id in self.library_database['books']:
            self.remove_book(book_id)
            self.add_book(new_book_id, new_title, new_author, new_year)
            write_json(self.path, self.library_database)
            self.event_manager.notify('update_book',
                                      f'Данные книги под ID: {book_id} обновлены: {new_title} {new_author} {new_year}')

    def add_reader(self, reader_id, name, email):
        """Добавляет читателя в базу данных."""
        create_reader = self.reader.create_reader(reader_id, name, email)
        self.library_database['readers'][reader_id] = create_reader.__dict__
        write_json(self.path, self.library_database)
        self.event_manager.notify('add_reader', f'Читатель добавлен: {name}')

    def remove_reader(self, reader_id):
        """Удаляет читателя из базы данных."""
        if reader_id in self.library_database['readers']:
            data = self.library_database['readers'].pop(reader_id)
            write_json(self.path, self.library_database)
            self.event_manager.notify('remove_reader', f'Удален читатель с номер ID: {data}')
        else:
            self.event_manager.notify('remove_reader',
                                      f'Попытка удалить читателя по ID: {reader_id}: читатель не найден.')

    def update_reader(self, reader_id, new_reader_id, new_name, new_email):
        """Обновляет данные читателя."""
        if reader_id in self.library_database['readers']:
            self.remove_reader(reader_id)
            self.add_reader(new_reader_id, new_name, new_email)
            write_json(self.path, self.library_database)
            self.event_manager.notify('update_reader',
                                      f'Данные читателя под ID: {reader_id} '
                                      f'обновлены: {new_reader_id} {new_name} {new_email}')

    def borrow_book(self, reader_name, book_title):
        """Выдает книгу читателю."""
        reader_id = find_entity_id(self.library_database, 'readers', 'name', reader_name)
        book_id = find_entity_id(self.library_database, 'books', 'title', book_title)
        if not reader_id:
            self.event_manager.notify('borrow_book', f'Читатель {reader_name} в базе не найден.')
            return
        if not book_id:
            self.event_manager.notify('borrow_book',
                                      f'Отказ на выдачу книги {book_title} для читателя {reader_name}: '
                                      f'книга не найдена в базе.')
            return
        book = self.library_database['books'].get(book_id)
        if book.get('available', False):
            book['available'] = False
        else:
            self.event_manager.notify('borrow_book',
                                      f'Отказ на выдачу книги {book_title} для читателя {reader_name}: '
                                      f'книга выдана ранее другому читателю.')
            write_json(self.path, self.library_database)
            return None
        self.library_database['borrowed_book'][book_id] = reader_id
        write_json(self.path, self.library_database)
        self.event_manager.notify('borrow_book', f'Книга {book_title} выдана читателю {reader_name}')

    def return_book(self, reader_name, book_title):
        """Возвращает книгу в библиотеку."""
        reader_id = find_entity_id(self.library_database, 'readers', 'name', reader_name)
        book_id = find_entity_id(self.library_database, 'books', 'title', book_title)
        if not reader_id:
            self.event_manager.notify('return_book', f'Читатель {reader_name} в базе не найден.')
            return
        if not book_id:
            self.event_manager.notify('return_book', f'Попытка вернуть книгу {book_title}, '
                                                     f'читателем {reader_name}, такой книги нет в базе.')
            return
        book = self.library_database['books'].get(book_id)
        if not book.get('available', False):
            book['available'] = True
        self.library_database['borrowed_book'].pop(book_id, None)
        write_json(self.path, self.library_database)
        self.event_manager.notify('return_book', f'Книга {book_title} возвращена читателем {reader_name}')

    def set_search_strategy(self, strategy):
        """Устанавливает стратегию поиска книг."""
        self.search_strategy = strategy

    def search_books(self, search_value):
        """Ищет книги по заданному критерию."""
        if not self.search_strategy:
            return 'Не выбрана стратегия поиска.'
        result = self.search_strategy.search(self.library_database['books'], search_value)
        if result:
            return result
        return f'Книги не найдена.'
