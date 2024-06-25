from typing import List

from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)


class TextSplitter:
    """TextSplitter class to split documents into chunks of text."""

    def __init__(
        self,
        chunk_size: int = 300,
        chunk_overlap: int = 0,
        splitter_type: str = "RecursiveCharacterTextSplitter",
    ):
        self.splitter = self._initialize_splitter(
            chunk_size, chunk_overlap, splitter_type
        )

    def _initialize_splitter(
        self, chunk_size: int, chunk_overlap: int, splitter_type: str
    ):
        """Initialize the splitter based on the splitter_type.

        Args:
            chunk_size (int): chunk size to split the text
            chunk_overlap (int): chunk overlap to split the text
            splitter_type (str): type of splitter to use

        Raises:
            ValueError: if the splitter_type is not recognized

        Returns:
            splitter: initialized splitter object
        """
        if splitter_type == "RecursiveCharacterTextSplitter":
            return RecursiveCharacterTextSplitter(
                chunk_size=chunk_size, chunk_overlap=chunk_overlap
            )
        elif splitter_type == "CharacterTextSplitter":
            return CharacterTextSplitter(
                chunk_size=chunk_size, chunk_overlap=chunk_overlap
            )
        else:
            raise ValueError(
                f"Unknown splitter type: {splitter_type}. Please choose from 'CharacterTextSplitter' or 'RecursiveCharacterTextSplitter'."
            )

    def __call__(self, documents: List[str]):
        """Split the documents into chunks of text.

        Args:
            documents (List[str]): list of documents to split
        """
        return self.splitter.split_documents(documents)
