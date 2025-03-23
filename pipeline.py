from scrape_pipeline.scraper import WebCrawler
import glob, os
from vector_db.create_vector_store import create_and_store_embeddings


def crawl_pipeline(url):
    """Pipeline to crawl website and update status."""
    # Create an instance of WebCrawler
    crawler = WebCrawler(url)

    # Start the crawling and saving process
    status = crawler.crawl_and_save()
    return status

def db_pipeline():
    """Pipeline to update db."""
    # Find the latest text content 
    all_files = glob.glob("./scraped_files/*")
    latest_file = max(all_files, key = os.path.getctime)
    print(f"Injecting to vector db : {latest_file}")

    # Start saving file to DB
    status = create_and_store_embeddings(file_path=latest_file)
    return status
