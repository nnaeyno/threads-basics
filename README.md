# Threads
## Overview
multi-threaded and async data fetching and JSON writing utility. <br> It fetches data from multiple URLs concurrently using threading, processes it, and writes the data to a JSON file. <br> The final JSON file is formatted as a valid JSON array of objects.

## Results and comparisons:
* Data successfully fetched from https://jsonplaceholder.typicode.com/posts/ and saved to _async_data.json_. **0.4647059440612793 seconds**
* Data successfully fetched from https://jsonplaceholder.typicode.com/posts/ and saved to _thread_data.json_. **0.39253807067871094 seconds**

## Features
1. **Concurrent Data Fetching:** Uses multiple threads or concurrency to fetch data from multiple URLs simultaneously, improving performance and efficiency.
2. **JSON Formatting:** Writes fetched data into a JSON file in a structured format, with proper handling of JSON arrays.
3. **File Handling:** Automatically creates the JSON file if it does not exist and ensures correct JSON formatting by managing commas and brackets.
## Components
* **DataFetcher**: Interface for fetching data from a URL. It can be implemented to fetch data in various formats. 
* **JSONDataWriter**: Handles writing data to a JSON file, ensuring the file starts as an array and is properly formatted. 
* **MultiThreadDataProcessor**: Manages multi-threaded fetching and writing of data. Ensures proper synchronization and file finalization.
* **AsyncDataProcessor**: Manages asynchronous fetching and writing of data. Ensures proper synchronization and file finalization.
## Requirements
* Python 3.11
* requests library for HTTP requests
* json and os libraries for JSON handling and file operations
* threading and concurrent.futures libraries for multi-threading

