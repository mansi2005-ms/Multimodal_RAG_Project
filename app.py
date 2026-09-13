import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

pdf_path = "data/sample.pdf"
if not os.path.exists(pdf_path):
    print("Error: sample.pdf not found in data folder.")
else:
    print("Loading PDF...")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print("Splitting document into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    print(f"Total chunks created: {len(chunks)}")

    print("Generating embeddings and storing in ChromaDB...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma.from_documents(chunks, embeddings, persist_directory="./db")
    print("Success! Embeddings stored in ChromaDB database.")