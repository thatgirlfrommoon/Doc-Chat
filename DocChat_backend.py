import chromadb
import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI()

# Function to get embedidngs from openai
def get_embedding(text):
    """ Create text embeddings."""
    print("creating embedding...")
    response = client.embeddings.create(
        input=text,
    model=os.getenv("OPENAI_EMBEDDING_MODEL"),

    )
    if not response.data[0].embedding:
        print("Failed to create embedding")
    print("Created embedding!")
    return response.data[0].embedding
    

def get_collection():
    """Initialise the chroma db client."""
    # initialise chromadb
    db_client = chromadb.PersistentClient(path='./VectorDB/vectorstore')
    collection = db_client.get_or_create_collection("crawled_docs_1")
    return collection

def generate_response_from_vectordb(user_query):
    """Create embeddings for user query and find response from vector store."""

    collection = get_collection()
    query_embedding = get_embedding(user_query)
    collection_results =  collection.query(
        query_embeddings = [query_embedding],
        n_results = 2
    )
    print("collection_results  : ",collection_results) 
    return (collection_results["documents"][0]) if collection_results["documents"] else ""


def chat_with_bot(user_input, args, conversation_history):
    """Create prompts to converse with llm."""

    retrieved_docs = generate_response_from_vectordb(user_input)
    # print("retrieved_docs   : ", retrieved_docs)
    context = "---- context ----\n".join(retrieved_docs)
    

    prompt = f""" 
    You are a helpful assistant.
    Please answer the question from the user based on the context given below. 
    Use only the information provided in the context.
    If you don't know the answer, you can say "I don't know".
    -----------------------------------------------------------------------------------------------------
    # Question
    {user_input}
    ------------------------------------------------------------------------------------------------------
    # Context
    {context}
    ------------------------------------------------------------------------------------------------------
    # Answer

    """ 
    # print(prompt)
    # Send the prompt to OpenAI's chat-based model (e.g., gpt-3.5-turbo, gpt-4)
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),  # Or use "gpt-4" for GPT-4 model
        messages=conversation_history + [{"role": "user", "content": prompt}],
        temperature=args["temperature"],  # Control randomness of the response (higher = more random)
        max_tokens=args["max_tokens"],  # Limit on tokens per response
    )

    # Extract the assistant's reply
    bot_message = response.choices[0].message.content
    return bot_message
