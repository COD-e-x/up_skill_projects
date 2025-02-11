from datetime import datetime

def get_formatted_current_time():
    """Возвращает текущее время в формате YYYY-MM-DD HH:MM:SS."""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')