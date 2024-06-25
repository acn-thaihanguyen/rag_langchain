import os
from typing import List

from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from src.vector_db.vector_db_base import VectorDBBase


class PineConeVectorDB(VectorDBBase):
    """PineConeVectorDB class to interact with Pinecone Vector Store."""

    def __init__(
        self,
        embeddings: OpenAIEmbeddings,
        index_name: str,
        namespace: str,
    ):
        self._embeddings = embeddings
        self._index_name = index_name
        self._namespace = namespace
        self._vectorstore = None

    def build_db(self, documents: List[str]):
        """Build the Pinecone Vector Store with the given documents.

        Args:
            documents (_type_): _description_

        Returns:
            _type_: _description_
        """
        print(f"Going to add {len(documents)} documents to Pinecone")

        vectorstore = PineconeVectorStore.from_documents(
            documents,
            self._embeddings,
            index_name=self._index_name,
            namespace=self._namespace,
        )
        print("### Finished ingesting... ###")

        self._vectorstore = vectorstore
        return vectorstore

    def get_retriever(self, search_type: str = "similarity", **kwargs):

        docsearch = PineconeVectorStore(
            embedding=self._embeddings,
            index_name=self._index_name,
            namespace=self._namespace,
        )

        if search_type == "similarity":
            return docsearch.as_retriever(search_type="similarity", **kwargs)
        elif search_type == "knn":
            return docsearch.as_retriever(search_type="knn", **kwargs)
        else:
            raise ValueError(
                f"Unknown search type: {search_type}. Please choose from 'similarity' or 'knn'."
            )
