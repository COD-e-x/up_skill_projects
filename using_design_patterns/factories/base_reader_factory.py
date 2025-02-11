from abc import ABC, abstractmethod


class ReaderFactory(ABC):
    """Абстрактная фабрика читателей."""

    @abstractmethod
    def create_reader(self, *args, **kwargs):
        pass
