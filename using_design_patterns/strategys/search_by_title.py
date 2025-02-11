from using_design_patterns.strategys.base_search_strategy import SearchStrategy

class SearchByTitle(SearchStrategy):
    """Поиск книг по названию."""

    def search(self, books, search_value):
        return {k: v for k, v in books.items() if search_value.lower() in v.get('title', '').lower()}
