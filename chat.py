from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

print("==================================================")
print("   Multimodal RAG Chatbot - Interactive CLI       ")
print("==================================================")

db_path = "./db"
if not os.path.exists(db_path):
    print("Error: Vector database not found. Please run app.py first.")
else:
    print("Loading vector database...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma(persist_directory=db_path, embedding_function=embeddings)
    print("Database loaded successfully! You can now start chatting.\n")

    while True:
        query = input("Ask a question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting chat. Good job on your project!")
            break

        if not query.strip():
            continue

        # Retrieve matching context from ChromaDB
        results = vector_store.similarity_search(query, k=2)

        print("\n--- Retrieved Context from RAG Pipeline ---")
        if results:
            for i, doc in enumerate(results):
                print(f"[{i+1}] {doc.page_content}")
        else:
            print("No relevant context found in the knowledge base.")
        print("-" * 45 + "\n")