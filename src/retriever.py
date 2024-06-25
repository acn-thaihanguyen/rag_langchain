from typing import Any, Dict, List

from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI

from src.const import INDEX_NAME, NAME_SPACE
from src.model.llms import load_embedding_model, load_llm
from src.vector_db.pinecone_db import PineConeVectorDB

# Load environment variables from a .env file
load_dotenv()


def run_llm(query: str, chat_history: List[Dict[str, Any]] = []) -> Dict[str, Any]:
    """
    Run a language model query with a conversational retrieval chain.

    Args:
        query (str): The input question/query for the language model.
        chat_history (List[Dict[str, Any]], optional): A list of dictionaries representing the chat history.
                                                      Each dictionary should contain the previous user inputs
                                                      and model responses. Defaults to an empty list.

    Returns:
        Dict[str, Any]: A dictionary containing the answer from the language model and source documents.
    """
    # Initialize OpenAI embeddings
    # embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    embeddings = load_embedding_model("openai")

    # Initialize PineCone vector database with the embeddings
    docsearch = PineConeVectorDB(
        embeddings=embeddings, index_name=INDEX_NAME, namespace=NAME_SPACE
    )

    # Initialize the OpenAI chat model
    chat = load_llm("gpt-3.5")

    # Create a conversational retrieval chain
    qa = ConversationalRetrievalChain.from_llm(
        llm=chat, retriever=docsearch.get_retriever(), return_source_documents=True
    )

    # Invoke the chain with the query and chat history
    return qa.invoke({"question": query, "chat_history": chat_history})


# if __name__ == "__main__":
#     # Example query to test the function
#     query = "What is the Attention Mechanism?"
#     response = run_llm(query)
#     print(f"Answer: {response.get("answer")}")
#     print(f"Source: {response.get("source_documents")[0].metadata}")
