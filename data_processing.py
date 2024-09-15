from abc import ABC, abstractmethod


class DataFetcher(ABC):
    @abstractmethod
    def fetch(self, url: str) -> dict:
        pass


class DataWriter(ABC):
    @abstractmethod
    def write(self, data: dict, output_file: str):
        pass


class DataProcessor(ABC):
    def __init__(self, fetcher: DataFetcher, writer: DataWriter):
        self.fetcher = fetcher
        self.writer = writer

    @abstractmethod
    def process(self, urls: list, output_file: str, max_workers: int = 16):
        pass

    @abstractmethod
    def worker(self, url: str, file_path: str):
        pass
