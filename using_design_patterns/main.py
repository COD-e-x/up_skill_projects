from using_design_patterns.facade.librarian_facade import LibrarianFacade
from using_design_patterns.entities.librarian import Librarian
from using_design_patterns.observers.text_writer_listener import TextWriteListener
from using_design_patterns.factories.printed_book_factory import PrintedBookFactory
from using_design_patterns.factories.core_reader_factory import CoreReaderFactory
from using_design_patterns.managers.event_manager import EventManager

if __name__ == '__main__':

    if __name__ == '__main__':
        t = TextWriteListener()

        b = PrintedBookFactory()
        r = CoreReaderFactory()
        e = EventManager()
        l = Librarian(b, r, e)
        lf = LibrarianFacade(l)

        # listener
        lf.subscribe('add_book', t)
        lf.subscribe('remove_book', t)
        lf.subscribe('update_book', t)
        lf.subscribe('add_reader', t)
        lf.subscribe('remove_reader', t)
        lf.subscribe('update_reader', t)
        lf.subscribe('borrow_book', t)
        lf.subscribe('return_book', t)

        # book
        lf.add_book('b-001', 'book 01', 'author 01', 2000)
        lf.add_book('b-002', 'book 02', 'author 02', 2001)
        lf.add_book('b-003', 'book 03', 'author 03', 2002)
        lf.remove_book('b-002')
        lf.update_book('b-003', 'b-004', 'book 04', 'autor 04', 2004)
        lf.add_book('b-005', 'book 05', 'author 05', 2003)
        lf.add_book('b-006', 'book 06', 'author 06', 2000)

        # reader
        lf.add_reader('r-001', 'reader 01', 'e-mal 01')
        lf.add_reader('r-002', 'reader 02', 'e-mal 02')
        lf.add_reader('r-003', 'reader 03', 'e-mal 03')
        lf.add_reader('r-004', 'reader 04', 'e-mal 04')
        lf.remove_reader('r-003')
        lf.update_reader('r-004', 'r-005', 'reader 05', 'e-mal 05')


        # выдача и возврат книги (реализованы как добавление в базу и удаление из нее)
        lf.borrow_book('reader 01', 'book 03')
        lf.return_book('reader 01', 'book 03')
        lf.borrow_book('reader 04', 'book 03')
        lf.borrow_book('reader 05', 'book 01')
        lf.borrow_book('reader 05', 'book 04')
        lf.borrow_book('reader 01', 'book 05')
        lf.return_book('reader 01', 'book 03333')

        # strategy (вывод терминал)
        print(lf.search_books_by_title('book 022'))
        print(lf.search_books_by_title('book 03'))
        print(lf.search_books_by_author('author 06'))
        print(lf.search_books_by_year(2000))
