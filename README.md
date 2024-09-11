# web-scraping-basics
## Overview
multi-threaded data fetching and JSON writing utility. <br> It fetches data from multiple URLs concurrently using threading, processes it, and writes the data to a JSON file. <br> The final JSON file is formatted as a valid JSON array of objects.

## Features
1. **Concurrent Data Fetching:** Uses multiple threads to fetch data from multiple URLs simultaneously, improving performance and efficiency.
2. **JSON Formatting:** Writes fetched data into a JSON file in a structured format, with proper handling of JSON arrays.
3. **File Handling:** Automatically creates the JSON file if it does not exist and ensures correct JSON formatting by managing commas and brackets.
## Components
* **DataFetcher**: Interface for fetching data from a URL. It can be implemented to fetch data in various formats. 
* **JSONDataWriter**: Handles writing data to a JSON file, ensuring the file starts as an array and is properly formatted. 
* **MultiThreadDataProcessor**: Manages multi-threaded fetching and writing of data. Ensures proper synchronization and file finalization.
## Requirements
* Python 3.6+
* requests library for HTTP requests
* json and os libraries for JSON handling and file operations
* threading and concurrent.futures libraries for multi-threading

