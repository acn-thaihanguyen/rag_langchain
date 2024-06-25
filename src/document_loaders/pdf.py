import os
from typing import List

import fitz  # PyMuPDF
from langchain_core.documents import Document

from src.document_loaders.base import BaseLoader


class PDFLoader(BaseLoader):
    """Class for loading PDF files into Document objects."""

    def __init__(self, file_path: str):
        super().__init__(file_path)

    def load(self) -> List[Document]:
        """Load the PDF file into Document objects.

        Returns:
            List[Document]: List of Document objects.
        """
        documents = []
        pdf_document = fitz.open(self.file_path)

        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            text = page.get_text()
            metadata = {"source": self.file_path, "page_number": page_number + 1}
            document = Document(page_content=text, metadata=metadata)
            documents.append(document)

        return documents


class FolderPDFLoader:
    """Class for loading all PDF files in a folder into Document objects."""

    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def load(self) -> List[Document]:
        """Load all PDF files in the folder into Document objects.

        Returns:
            List[Document]: List of Document objects.
        """
        all_documents = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".pdf"):
                file_path = os.path.join(self.folder_path, filename)
                pdf_loader = PDFLoader(file_path)
                documents = pdf_loader.load()
                all_documents.extend(documents)
        return all_documents
