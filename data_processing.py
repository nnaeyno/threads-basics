import requests
import json
from abc import ABC, abstractmethod


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


class JSONDataWriter(DataWriter):
    def write(self, data: dict, output_file: str):
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)


class MultiThreadDataProcessor:
    def __init__(self, fetcher: DataFetcher, writer: DataWriter):
        self.fetcher = fetcher
        self.writer = writer

    def process(self, url: str, output_file: str):
        data = self.fetcher.fetch(url)
        self.writer.write(data, output_file)

