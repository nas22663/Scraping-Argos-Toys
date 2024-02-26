# Argos Toys Spider

This Scrapy project is designed to scrape product information from the toys section of the Argos website
, specifically targeting toys suitable for children aged 5 to 8 years. It extracts product names, prices, and URLs for further details,
navigating through pagination to collect data across multiple pages.

## Project Structure

The project includes the following key components:

- `ArgosSpider`: The main spider for scraping the Argos website.
- `items.py`: Defines the `ArgosToysItem` class for storing extracted data.
- `middlewares.py` and `settings.py`: Configure the Scrapy settings and middlewares, including user-agent strings and concurrent request settings.
- `pipelines.py`: (Optional) Define item processing pipelines if needed for further data processing or saving to databases.

## Features

- **Product Data Extraction**: Extracts names, prices, and product detail URLs.
- **Pagination Handling**: Automatically navigates through pagination to extract data from multiple pages.
- **JavaScript Rendering Support**: Initially set up to use Splash for JavaScript rendering, ensuring dynamic content is loaded. This setup can be adjusted based on the project's needs.#Not Necessary in my experience

## Setup

To run this project, you need Python 3 and Scrapy installed on your system. If you wish to use Splash for JavaScript rendering, you'll also need Docker to run the Splash service.

1. **Install Scrapy**:
   
   ```sh
   pip install scrapy
