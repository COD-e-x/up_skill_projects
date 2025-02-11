from abc import ABC, abstractmethod

class BookFactory(ABC):
    """Абстрактная фабрика книг."""

    @abstractmethod
    def create_book(self, *args, **kwargs):
        pass