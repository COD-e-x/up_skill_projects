from using_design_patterns.observers.event_listeners import EventListeners
from using_design_patterns.utils.datetime_utils import get_formatted_current_time


class TextWriteListener(EventListeners):
    """Слушатель для записи логов при добавлении книги в log_text.txt."""

    def update(self, message):
        data = f'{get_formatted_current_time()}: {message}'
        with open(r'./data/log_text.txt', 'a', encoding='utf-8') as f:
            f.write(data)
            f.write('\n')
