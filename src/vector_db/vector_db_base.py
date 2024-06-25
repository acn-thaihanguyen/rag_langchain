from abc import ABC, abstractmethod
from typing import List


class VectorDBBase(ABC):
    """VectorDBBase class to define the interface for the VectorDB classes."""

    @abstractmethod
    def build_db(self, documents: List[str]):
        pass

    @abstractmethod
    def get_retriever(self, search_type: str = "similarity", **kwargs):
        pass
