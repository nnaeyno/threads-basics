import asyncio
import os
import time
from async_data_processing import AsyncDataProcessor, AsyncJSONDataWriter, AsyncDataFetcher
from threaded_data_processing import URLDataFetcher, JSONDataWriter, MultiThreadDataProcessor


def construct_urls(base_url: str):
    result = []
    for i in range(1, 78):
        result += [base_url + str(i)]
    return result


def thread_main(output_file, urls, max_workers):
    start_time = time.time()

    fetcher = URLDataFetcher()
    writer = JSONDataWriter()

    processor = MultiThreadDataProcessor(fetcher, writer)

    try:
        processor.process(urls, output_file, max_workers)
        print(
            f"Data successfully fetched from {base_url} and saved to {output_file}. {time.time() - start_time} seconds")
    except Exception as e:
        print(f"An error occurred: {e}")


async def async_main(output_file, urls, max_workers):
    start_time = time.time()

    fetcher = AsyncDataFetcher()
    writer = AsyncJSONDataWriter()

    processor = AsyncDataProcessor(fetcher, writer)

    try:
        await processor.process(urls, async_output_file, max_workers)
        print(
            f"Data successfully fetched from {base_url} and saved to {output_file}. {time.time() - start_time} seconds")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the main process
if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/posts/"
    async_output_file = "async_data.json"
    thread_output_file = "thread_data.json"
    num_workers = 78
    api_urls = construct_urls(base_url)
    asyncio.run(async_main(async_output_file, api_urls, num_workers))
    thread_main(thread_output_file, api_urls, num_workers)
