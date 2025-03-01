import scrapy
import os
import html2text
from urllib.parse import urlparse


class DoccrawlerSpider(scrapy.Spider):
    name = "document_spider"
    allowed_domains = ["huggingface.co"]
    start_urls = [
                #   "https://huggingface.co/docs/transformers/en/index", 
                #   "https://huggingface.co/blog/LLMhacker/deepseek-r-is-best",
                  "https://huggingface.co/docs/diffusers/en/index",
                    # "https://huggingface.co/docs/diffusers/en/quicktour",
                ]

    def __init__(self, *args, **kwargs):
        super(DoccrawlerSpider, self).__init__(*args, **kwargs)
        if 'start_url' in kwargs:
            self.start_urls = [kwargs.get('start_url')]

        # Create an output folder to dump results
        if not os.path.exists('./../scraped_files'):
            os.makedirs('./../scraped_files')

        # Initialize HTML to text converter
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = True
        self.converter.ignore_images = True
        self.converter.ignore_emphasis = True

    def parse(self, response):
        # Extract page title and body text
        text = self.converter.handle(response.body.decode('utf-8'))
        text = text.replace('<|endoftext|>', ' ')

        # clean up the text
        url = response.url.strip("/")

        #generate randon filename using hashvalue of url
        filename = f"./../scraped_files/doc_{hash(url)}.txt"
        
        # Write extracted content to a file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        
