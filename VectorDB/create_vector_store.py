import chromadb
from openai import OpenAI
from langchain_text_splitters import TokenTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

# Function to get embedidngs from openai
def get_embedding(text):
    """Create text embeddings."""
    print("Creating embedding...")
    client = OpenAI()
    response = client.embeddings.create(
        input=text, model=os.getenv("OPENAI_EMBEDDING_MODEL")
    )
    if not response.data[0].embedding:
        print("Failed to create embedding")
    print("Created embedding!")
    return response.data[0].embedding


def get_collection():
    """Initialise the chroma db client."""
    # initialise chromadb
    client = chromadb.PersistentClient(path="./vectorstore")
    collection = client.get_or_create_collection("crawled_docs_1")
    return collection


def store_embedding(embedding, chunk, id):
    """Store the embeddings"""
    collection = get_collection()
    collection.add(
        embeddings=[embedding],
        documents=[chunk],
        metadatas=[{"source": f"chunk_{id}"}],
        ids=[f"doc_{id}"],
    )
    print(f"stored chunk : {id}")


# Create embeddings
def create_and_store_embeddings():
    """Create and store text embeddings."""

    # load text file
    dir_path = "./../scraped_files/"
    txt_files = [f for f in os.listdir(dir_path) if f.endswith(".txt")]
    if len(txt_files) != 1:
        raise ValueError("Should be only one txt file in the current directory")
    filename = txt_files[0]
    with open(dir_path + filename, encoding="utf-8") as file:
        doc_text = file.read()

    # split text into chunks
    chunk_size = 500
    text_splitter = TokenTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=100,
    )
    chunks = text_splitter.split_text(doc_text)

    # create embeddings for each chunk
    for id, chunk in enumerate(chunks):
        # vectorize each chunk and store
        print(len(chunk))
        embedding = get_embedding(chunk)
        store_embedding(embedding, chunk, id)


if __name__ == "__main__":
    create_and_store_embeddings()
    print("Created vector embeddings and stored in a chromadb collection...")
