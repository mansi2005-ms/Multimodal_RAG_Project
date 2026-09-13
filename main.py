import os
from PIL import Image
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

print("==========================================")
print("   Multimodal RAG Project - Main Runner   ")
print("==========================================")

# 1. Verify Assets
pdf_path = "data/sample.pdf"
image_path = "data/sample.jpg"

if os.path.exists(pdf_path):
    print("[PASS] sample.pdf found in data folder.")
else:
    print("[FAIL] sample.pdf missing!")

if os.path.exists(image_path):
    print("[PASS] sample.jpg found in data folder.")
    img = Image.open(image_path)
    print(f"       Image Info -> Format: {img.format}, Size: {img.size}")
else:
    print("[FAIL] sample.jpg missing!")

# 2. Query Vector Database
db_path = "./db"
if os.path.exists(db_path):
    print("\nLoading vector database from ChromaDB...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma(persist_directory=db_path, embedding_function=embeddings)

    query = "What is the Multimodal RAG chatbot designed for?"
    print(f"Running Test Query: '{query}'")

    results = vector_store.similarity_search(query, k=1)
    if results:
        print("\n--- Retrieved Knowledge Base Context ---")
        print(results[0].page_content)
    else:
        print("No matching context found.")
else:
    print("\nVector database not found. Please run app.py first.")

print("\n==========================================")
print("   Pipeline execution completed successfully!  ")
print("==========================================")