from json import dump, load, JSONDecodeError


def read_json(file_path):
    """Стандартная функция для чтения JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return load(f)
    except (FileNotFoundError, JSONDecodeError):
        return {}


def write_json(file_path, data):
    """Стандартная функция для записи данных в JSON файл."""
    with open(file_path, 'w', encoding='utf-8') as f:
        dump(data, f, indent=2, ensure_ascii=False)