from abc import ABC, abstractmethod


class SearchStrategy(ABC):
    """Стратегия поиска информации"""
    @abstractmethod
    @abstractmethod
    def search(self, books, search_value):
        pass
