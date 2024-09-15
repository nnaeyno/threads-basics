import requests

from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, urls: list, output_file: str, max_workers: int = 16):
        pass

    @abstractmethod
    def worker(self, url: str, file_path: str):
        pass


class DataFetcher(ABC):
    @abstractmethod
    def fetch(self, url: str) -> dict:
        pass


class DataWriter(ABC):
    @abstractmethod
    def write(self, data: dict, output_file: str):
        pass


class URLDataFetcher(DataFetcher):
    def fetch(self, url: str) -> dict:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Failed to fetch data from {url}, status code: {response.status_code}")
