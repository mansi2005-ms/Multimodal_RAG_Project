# Multimodal RAG Chatbot
An end-to-end Retrieval-Augmented Generation (RAG) system built with Python, LangChain, ChromaDB, HuggingFace embeddings, and Pillow for multimodal processing.

## Project Structure
- `app.py`: Handles PDF document loading, text chunking, embedding generation, and ChromaDB vector persistence.
- `query.py`: Performs semantic similarity searches against the vector database.
- `multimodal.py`: Handles image asset validation and multimodal integration.
- `chat.py`: Provides an interactive command-line interface to query the knowledge base.

## 📂 Additional Documentation & Folders
- `assets/`: Contains project posters, logos, and banners.
- `Material/`: Contains project presentation PPT and detailed documentation PDF.
- `notes/`: Architectural notes and technical documentation.
- `resources/`: Reference materials and research documentation.

## Setup & Execution
1. Install dependencies: `pip install -r requirements.txt`
2. Run data ingestion: `python app.py`
3. Start the interactive chat: `python chat.py`