import os
from argparse import ArgumentParser

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

from src.const import INDEX_NAME, NAME_SPACE
from src.document_loaders.pdf import FolderPDFLoader as FolderPDFLoaderTest
from src.model.llms import load_embedding_model
from src.splitters.text_splitter import TextSplitter
from src.vector_db.pinecone_db import PineConeVectorDB

load_dotenv()


def main(folder_name: str):
    # Define the path to the PDF folder
    pdf_folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "data_source", folder_name
    )
    print(f"Loading PDFs from: {pdf_folder}")

    # Load PDF files
    pdf_loader = FolderPDFLoaderTest(pdf_folder)
    pdf_files = pdf_loader.load()

    # Split text
    text_splitter = TextSplitter()
    documents = text_splitter(pdf_files)

    # Update metadata for each document
    for doc in documents:
        source_pdf = (
            doc.metadata["source"].split("/")[-1].replace("_", " ").replace(".pdf", "")
        )
        doc.metadata.update({"source": source_pdf})

    # Initialize embeddings
    # TODO: Currently it is not possible to use GoogleAPI with current PineCone setup. Add support for GoogleAPI embeddings.
    embeddings = load_embedding_model("openai")

    # Initialize and build the vector store
    pc = PineConeVectorDB(
        embeddings=embeddings,
        index_name=INDEX_NAME,
        namespace=NAME_SPACE,
    )
    _ = pc.build_db(documents=documents)

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Process PDFs and build a Pinecone vector store."
    )
    parser.add_argument(
        "folder_name", type=str, help="Name of the folder containing PDF files"
    )
    args = parser.parse_args()
    main(args.folder_name)
