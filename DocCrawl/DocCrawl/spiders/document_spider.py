import scrapy
import os
import html2text
from urllib.parse import urlparse
from datetime import datetime
import pandas as pd


class DoccrawlerSpider(scrapy.Spider):
    name = "document_spider"
    allowed_domains = ["huggingface.co"]
    start_urls = [
                  "https://huggingface.co/docs/transformers/en/index", 
                  "https://huggingface.co/blog/LLMhacker/deepseek-r-is-best",
                  "https://huggingface.co/docs/diffusers/en/index",
                  "https://huggingface.co/docs/diffusers/en/quicktour",
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

    def get_domain_and_path_from_url(self, url):
        """" This function extracts the domain and path from the URL. """
        parsed_uri = urlparse(url)
        domain = parsed_uri.netloc
        path = parsed_uri.path.strip("/")

        sanitised_path = path.replace("/", "_").replace(" ", "_")
        return domain,sanitised_path
    
    def save_url(self, url, file_path):
        """ This function saves the crawled URLs to a file """
        
        url_df = pd.DataFrame( [{"url": url }])
        if not os.path.exists(file_path):
            url_df.to_csv(file_path, 
                          index=False)
        else:
            urls_df_store = pd.read_csv(file_path)
            if url not in urls_df_store["url"].values:
                url_df.to_csv(file_path, 
                              mode='a', header=False, index=False)
            else:
                print(f"URL: {url} has been already crawled. Hence skipping...")
                return
        return 1

    def parse(self, response):
        """ This function extracts the content of the page and writes it to a file """
        # Extract page title and body text
        text = self.converter.handle(response.body.decode('utf-8'))
        text = text.replace('<|endoftext|>', ' ')

        # Save the URL
        url_file = "./../scraped_files/urls.csv"
        if self.save_url(response.url, url_file):
            # clean up the text
            url = response.url.strip("/")
            domain, path = self.get_domain_and_path_from_url(url)
            time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")

            #generate randon filename using hashvalue of url
            filename = f"./../scraped_files/doc_{domain[:5]}_{path}_{time_stamp}.txt"

            
            # Write extracted content to a file
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)
        
