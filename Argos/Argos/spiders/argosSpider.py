import scrapy
import re
import json
from Argos.items import ArgosToysItem  # Adjust the import path as per your project structure

class ArgosSpider(scrapy.Spider):
    name = 'argos'
    allowed_domains = ['argos.co.uk']
    start_urls = ['https://www.argos.co.uk/list/5-to-8-years-toys?tag=ar:browse:clp:toys:m052:image:5-to-8-years']

    def parse(self, response):
        script_content = response.xpath('//script[contains(., "window.App")]/text()').get()
        if script_content:
            yield from self.extract_items_from_script(script_content)
        else:
            self.logger.error("Failed to find the script tag containing 'window.App'.")

        next_page_url = response.css('a[data-test="component-pagination-arrow-right"]::attr(href)').get()
        if next_page_url:
            yield response.follow(next_page_url, self.parse)

    def extract_items_from_script(self, script_content):
        match = re.search(r'window\.App\s*=\s*(\{.*?\})(;|\s*$)', script_content, re.DOTALL)
        if match:
            json_str = match.group(1)
            try:
                data = json.loads(json_str)
                products = data.get('redux', {}).get('product', {}).get('products', [])
                for product in products:
                    attributes = product.get('attributes', {})
                    item = ArgosToysItem()
                    item['name'] = attributes.get('name', 'N/A')
                    item['price'] = attributes.get('price', 'N/A')
                    # Construct product URL directly without storing productId separately
                    product_id = attributes.get('productId', 'N/A')
                    item['productUrl'] = f"https://www.argos.co.uk/product/{product_id}?clickCSR=slp:cannedSearch"
                    yield item
            except json.JSONDecodeError as e:
                self.logger.error(f"Failed to decode JSON: {e}")
