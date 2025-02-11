from using_design_patterns.factories.base_reader_factory import ReaderFactory
from using_design_patterns.entities.core_reader import CoreReader


class CoreReaderFactory(ReaderFactory):
    """Фабрика для основных читателей."""

    def create_reader(self, reader_id, name, email):
        return CoreReader(reader_id, name, email)
