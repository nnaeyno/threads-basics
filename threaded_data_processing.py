import threading
from concurrent.futures import ThreadPoolExecutor, wait
import json
from data_processing import DataWriter, DataProcessor, DataFetcher


class JSONDataWriter(DataWriter):
    def write(self, data: dict, output_file: str):
        with open(output_file, 'r+') as f:

            f.seek(0, 2)
            file_pos = f.tell()

            if file_pos == 0:
                f.write('[\n')
            else:
                f.seek(file_pos - 1)
                if f.read(1) == ']':
                    f.seek(file_pos - 2)
                else:
                    f.seek(file_pos - 1)

                f.write(',\n')

            json.dump(data, f, indent=4)
            f.write('\n]')


class MultiThreadDataProcessor(DataProcessor):

    def __init__(self, fetcher: DataFetcher, writer: DataWriter):
        self.fetcher = fetcher
        self.writer = writer
        self.lock = threading.Lock()

    def worker(self, url: str, file_path: str):
        data = self.fetcher.fetch(url)
        if data:
            with self.lock:  # this is very inefficient but the requirement said to save to file immediately
                self.writer.write(data, file_path)

    def process(self, urls: list, output_file: str, max_workers: int = 16):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(self.worker, url, output_file) for url in urls]
            wait(futures)
        self.finalize_json_file(output_file)

    def finalize_json_file(self, file_path: str):
        with self.lock:
            with open(file_path, 'rb+') as f:
                f.seek(-2, 2)
                if f.read(1) == ',':
                    f.seek(-2, 2)
                    f.truncate()
                f.write(b'\n]')
