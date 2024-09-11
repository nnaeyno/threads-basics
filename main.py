import time

from data_processing import JSONDataWriter, MultiThreadDataProcessor, URLDataFetcher


def construct_urls(base_url: str):
    result = []
    for i in range(1, 78):
        result += [base_url + str(i)]
    return result


if __name__ == "__main__":
    start_time = time.time()
    base_url = "https://jsonplaceholder.typicode.com/posts/"
    output_file = "data.json"

    fetcher = URLDataFetcher()

    writer = JSONDataWriter()

    processor = MultiThreadDataProcessor(fetcher, writer)
    urls = construct_urls(base_url)

    try:
        processor.process(urls, output_file)
        print(f"Data successfully fetched from {base_url} and saved to {output_file}. {time.time() - start_time} seconds")
    except Exception as e:
        print(f"An error occurred: {e}")
