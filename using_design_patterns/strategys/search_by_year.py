from using_design_patterns.strategys.base_search_strategy import SearchStrategy

class SearchByYear(SearchStrategy):
    """Поиск книг по году."""

    def search(self, books, search_value):
        return {k: v for k, v in books.items() if v.get('year') == search_value}
