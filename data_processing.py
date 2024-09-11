import threading
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor

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
        self.lock = threading.Lock()

    def worker(self, url: str, file_path: str):
        data = self.fetcher.fetch(url)
        if data:
            with self.lock:
                self.writer.write(data, file_path)

    def process(self, urls: list, output_file: str, max_threads: int = 16):
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = [executor.submit(self.worker, url, output_file) for url in urls]

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Exception during execution: {e}")
