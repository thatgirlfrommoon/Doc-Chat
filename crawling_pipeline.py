from scrape_pipeline.scraper import WebCrawler



def crawl_pipeline(url):
    """Pipeline to crawl website and update status"""
  
    # Create an instance of WebCrawler
    crawler = WebCrawler(url)

    # Start the crawling and saving process
    status = crawler.crawl_and_save()
    return status

def db_pipeline(url):
    """Pipeline to crawl website and update status"""
  
    # Create an instance of WebCrawler
    crawler = WebCrawler(url)

    # Start the crawling and saving process
    status = crawler.crawl_and_save()
    return status
