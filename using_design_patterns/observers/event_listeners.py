from abc import ABC, abstractmethod


class EventListeners(ABC):
    """Абстрактный класс для слушателей событий."""

    @abstractmethod
    def update(self, message):
        """Метод для обработки событий."""
        pass