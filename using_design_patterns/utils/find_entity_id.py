def find_entity_id(database, entity_type, key, value):
    """
    Находит ID сущности по заданному значению.

    :param database: База данных.
    :param entity_type: Тип сущности (пример: 'readers' или 'books').
    :param key: Ключ для поиска (пример: 'name' или 'title').
    :param value: Значение для поиска.
    :return: ID сущности или None, если не найдено.
    """
    for id_, data in database[entity_type].items():
        if data.get(key) == value:
            return id_
    return None

