import os
import requests
import csv
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import datetime as d
from scrape_pipeline.url_validator import validate_url

class WebCrawler:
    def __init__(self, url):
        self.url = url
        self.file_path = "scraped_files/"
        self.scraped_url_registry=self.file_path+"urls.csv"

    def fetch_content(self):
        """Fetch the content of the URL."""
        try:
            content = requests.get(self.url)
            
            # Check if the request was successful
            content.raise_for_status() 
            return content.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
            return None

    def extract_text(self, html_content):
        """Extract text content from HTML using BeautifulSoup."""
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text()
        cleaned_text = ' '.join(text_content.split())  # Clean up extra spaces
        return cleaned_text

    def genearate_full_path(self):
        domain = urlparse(self.url).netloc
        full_path = f"{self.file_path}{domain[:15]}_{d.now().strftime('%Y%m%d_%H%M%S')}.txt"
        return full_path


    def save_to_file(self, text_content):
        """Save the extracted text to a file."""
        try:
            if not os.path.exists(self.file_path):
                os.makedirs(self.file_path)
            full_file_path = self.genearate_full_path()
            with open(full_file_path, 'w', encoding='utf-8') as file:
                file.write(text_content)
            print(f"Text content saved to {full_file_path}")
        except Exception as e:
            print(f"Error saving the file: {e}")
    
    def url_in_registry(self):
        """Check if the URL is already present in the CSV file."""
        try:
            with open(self.scraped_url_registry, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['url'] == self.url:
                        return True
        except FileNotFoundError:
            # If the CSV file doesn't exist, return False
            return False
        return False

    def add_url_to_csv(self):
        """Add the crawled URL to the CSV file."""
        try:
            with open(self.scraped_url_registry, mode='a', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([self.url])
            print(f"URL added to {self.scraped_url_registry}")
        except Exception as e:
            print(f"Error adding URL to CSV: {e}")


    def crawl_and_save(self):
        """Crawl the URL, extract text, and save it to a file."""

        # validate URL
        validity = validate_url(self.url)
        print(validity)
        if not validity["valid"]:
            return validity
        if self.url_in_registry():
            print(f"URL '{self.url}' is already crawled. Skipping...")
            return 1
        else:
            html_content = self.fetch_content()
            if html_content:
                text_content = self.extract_text(html_content)
                self.save_to_file(text_content)
                self.add_url_to_csv()
                print(f"URL '{self.url}' is crawled.")
            return 2


