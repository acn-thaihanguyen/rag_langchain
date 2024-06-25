from abc import ABC, abstractmethod
from typing import List

from langchain_core.documents import Document


class BaseLoader(ABC):
    """Abstract base class for loaders."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def load(self) -> List[Document]:
        pass
