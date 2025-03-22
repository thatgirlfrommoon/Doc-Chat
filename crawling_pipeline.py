
from scrape_pipeline.scraper import WebCrawler

def pipeline(url):
    # Create an instance of WebCrawler
    crawler = WebCrawler(url)

    # Start the crawling and saving process
    status = crawler.crawl_and_save()
    return status
