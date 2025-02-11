class EventManager:
    """Менеджер для управления подписчиками на события."""

    def __init__(self):
        self.__listeners = {}

    def subscribe(self, event_type, listener):
        """Подписывает слушателя на событие."""
        if event_type not in self.__listeners:
            self.__listeners[event_type] = []
        self.__listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        """Удаляет слушателя из подписки на событие."""
        if event_type in self.__listeners and listener in self.__listeners[event_type]:
            self.__listeners[event_type].remove(listener)

    def notify(self, event_type, message):
        """Уведомляет слушателей о событии."""
        for listener in self.__listeners.get(event_type, []):
            listener.update(message)
