from data_processing import JSONDataWriter, MultiThreadDataProcessor, URLDataFetcher

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/"
    output_file = "posts.json"

    fetcher = URLDataFetcher()

    writer = JSONDataWriter()

    processor = MultiThreadDataProcessor(fetcher, writer)

    try:
        processor.process(url, output_file)
        print(f"Data successfully fetched from {url} and saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")
