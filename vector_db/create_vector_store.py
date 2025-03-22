import chromadb
from openai import OpenAI
from langchain_text_splitters import TokenTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

# Function to get embedidngs from openai
def get_embedding(text):
    """ Create text embeddings."""
    print("Creating embedding...")
    client = OpenAI()
    response = client.embeddings.create(
        input=text,
        model=os.getenv("OPENAI_EMBEDDING_MODEL")

    )
    if not response.data[0].embedding:
        print("Failed to create embedding")
    print("Created embedding!")
    return response.data[0].embedding

def get_collection():
    """Initialise the chroma db client."""
    store_path = './vector_db/vectorstore'
    if not os.path.exists(store_path):
        os.makedirs('')
    client = chromadb.PersistentClient(path=store_path)
    return client.get_or_create_collection("crawled_docs_1")


def store_embedding(embedding, chunk, chunk_id, collection):
    """Store the embeddings"""
    collection.upsert(
        embeddings=[embedding],
        documents=[chunk],
        metadatas=[{"source": chunk_id}],
        ids=[chunk_id]
    )
    print(f"stored chunk : {chunk_id}" )

# Create embeddings
def create_and_store_embeddings(file_path):
    """ Create and store text embeddings."""

    chunk_size = 5000
    status= {
        "process": False,
        "error_message": ""
    }
    try:
        text_splitter = TokenTextSplitter(chunk_size=chunk_size,
                                        chunk_overlap=100,)
        collection = get_collection()
        
        print(f"Processing file: {file_path}")
        with open(file_path, encoding="utf-8") as file:
            doc_text = file.read()

        # split the text into chunks
        chunks = text_splitter.split_text(doc_text)
        # create embeddings for each chunk
        for num,chunk in enumerate(chunks):
            embedding = get_embedding(chunk)
            store_embedding(embedding,chunk, f"{num}_{hash(file_path)}",
                            collection)
        print("Created vector embeddings and stored in a chromadb collection...")
        status["process"]= True
    except Exception as e:
        status["error_message"]= e
    return status


