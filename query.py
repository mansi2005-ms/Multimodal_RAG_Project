from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

print("Loading vector database...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = Chroma(persist_directory="./db", embedding_function=embeddings)

query = "What database is used for storing embeddings?"
print(f"\nUser Query: {query}")

print("\nSearching for relevant context...")
results = vector_store.similarity_search(query, k=2)

print("\n--- Retrieved Context ---")
for i, doc in enumerate(results):
    print(f"Result {i+1}: {doc.page_content}\n")