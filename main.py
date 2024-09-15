import time

from threaded_data_processing import JSONDataWriter, URLDataFetcher
from async_data_processing import AsyncDataProcessor, AsyncJSONDataWriter, AsyncDataFetcher


def construct_urls(base_url: str):
    result = []
    for i in range(1, 78):
        result += [base_url + str(i)]
    return result


if __name__ == "__main__":
    start_time = time.time()
    base_url = "https://jsonplaceholder.typicode.com/posts/"
    output_file = "data.json"
    urls = construct_urls(base_url)

    fetcher = AsyncDataFetcher()
    writer = AsyncJSONDataWriter()

    processor = AsyncDataProcessor(fetcher, writer)

    try:
        processor.process(urls, output_file)
        print(f"Data successfully fetched from {base_url} and saved to {output_file}. {time.time() - start_time} seconds")
    except Exception as e:
        print(f"An error occurred: {e}")
