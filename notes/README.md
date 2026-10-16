# Multimodal RAG Chatbot: Architecture Notes

**Project:** Ask Your Documents: The Multimodal RAG Chatbot
**Contributor:** Mansi Suresh Shirode (Volunteer, GudSky Research Foundation)
**Mentor:** Abhishek Kumar Shukla

---

## 1. Introduction

PDFs are easy to share but hard to search. Important information is often buried in long text and in images such as charts, diagrams, and figures. A normal keyword search cannot understand meaning, and it ignores images completely.

This project solves that problem with **Retrieval-Augmented Generation (RAG)**. The user uploads PDFs and asks questions in plain language. The system finds the most relevant parts of the documents, both text and images, and uses them to generate an accurate answer.

**Objective:** Transform static PDFs into searchable, context-aware knowledge bases that support queries over both text and embedded images.

---

## 2. What is RAG?

A Large Language Model (LLM) on its own answers only from what it learned during training. It does not know the content of your private documents, and it may make up facts (hallucination).

RAG fixes this in two parts:

- **Retrieval:** Find the pieces of the documents most relevant to the question.
- **Generation:** Give those pieces to the LLM as context, so the answer is based on the actual document.

**Why it matters here:**
- Answers are grounded in the uploaded documents.
- Hallucination is reduced.
- No model retraining is needed when documents change. Just ingest the new files.

---

## 3. Why Multimodal?

Many documents carry meaning in images, not just text. A multimodal system can process **text and visuals together**, so a user can ask about a chart or diagram and still get a relevant answer. A text-only RAG system would miss this information.

---

## 4. Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| Document Parsing | PyPDF, Pillow | Extract text and render images or visual elements from PDFs |
| Orchestration | LangChain | Document loading, text chunking, and retrieval pipelines |
| Embeddings & LLM | Multimodal LLM | Process text chunks and visual embeddings for semantic search |
| Vector Database | ChromaDB | Store and index embeddings for fast similarity search (top-`k`, `k = 2`) |
| Backend & Interface | Python, Flask | Web backend and API endpoints for chat |

### Role of each component

- **PyPDF:** Reads the PDF and pulls out the raw text, page by page.
- **Pillow:** Handles image processing, so images and visual elements from the PDF can be rendered and passed to the model.
- **LangChain:** The framework that connects all steps. It loads documents, splits text into chunks, and manages retrieval.
- **Multimodal LLM:** Understands both text and images. It creates embeddings for search and generates the final answer.
- **ChromaDB:** A vector database that stores embeddings and quickly finds the ones most similar to a query.
- **Flask:** A lightweight Python web framework that exposes the chatbot through API endpoints and a web interface.

---

## 5. RAG Pipeline: Step by Step

```text
PDF -> Parse -> Chunk -> Embed -> Store (ChromaDB)
                                      |
User Query -> Embed -> Similarity Search (k=2) -> LLM -> Answer
```

### Step 1: Document Ingestion and Chunking

- Input PDFs are parsed to extract both text and images.
- The text is split into smaller pieces called **chunks**:
  - **Chunk size:** 500 characters
  - **Overlap:** 50 characters

**Why chunk?** LLMs have limited context windows, and smaller chunks make retrieval more precise. A whole document is too large and too general to be useful as context.

**Why overlap?** Without overlap, a sentence or idea can be cut in half at a chunk boundary. The 50-character overlap repeats the end of one chunk at the start of the next, so context is preserved.

### Step 2: Embedding Generation

- Text chunks and extracted images are converted into **embeddings**, which are dense numerical vectors.
- Embeddings capture meaning. Texts with similar meaning get vectors that are close together, even if they use different words.
- These vectors are stored in ChromaDB.

### Step 3: Similarity Search (ChromaDB)

- When a user asks a question, the query is converted into an embedding in the same way.
- ChromaDB compares the query vector with all stored vectors and returns the **top `k = 2`** most similar chunks.

**About `k = 2`:** Only the two most relevant results are retrieved. This keeps the context short and focused. A larger `k` gives more coverage but adds noise and may include irrelevant content.

### Step 4: LLM Synthesis

- The retrieved chunks and images are sent to the Multimodal LLM together with the user's question.
- The LLM reads this context and writes a precise answer based on it.
- Because the answer comes from retrieved content, it is grounded and less likely to hallucinate.

---

## 6. Key Design Decisions

| Decision | Reason |
|---|---|
| Chunk size of 500 characters | Small enough for precise retrieval, large enough to keep meaning |
| Overlap of 50 characters | Prevents loss of context at chunk boundaries |
| `k = 2` retrieval | Keeps the LLM context focused and relevant |
| Multimodal LLM | Allows questions about images as well as text |
| ChromaDB | Simple and fast vector storage for similarity search |
| Flask backend | Lightweight and easy to expose as a web API |

---

## 7. Benefits

- Search by meaning, not just keywords.
- Works across both text and images in PDFs.
- Answers are grounded in the source documents.
- New documents can be added without retraining any model.

---

## 8. Repository Structure

```text
.
├── Material/        # Presentation PPT, documentation PDF, folder guides
├── assests/         # Project poster, logos (incl. GudSky Foundation logo), banners
├── data/            # Input data (PDFs and images)
├── db/              # ChromaDB vector database storage
├── notes/           # Architecture notes and technical documentation
├── README.md        # Project overview
├── app.py           # Flask application (web backend and chat API)
├── chat.py          # Chat logic
├── main.py          # Main entry point
├── make_image.py    # Script to generate images
├── make_pdf.py      # Script to generate PDFs
├── multimodal.py    # Multimodal (text + image) processing
└── query.py         # Querying and retrieval from the vector database
```

### Folders

| Folder | Contents |
|---|---|
| `Material/` | Project presentation, detailed documentation PDF, and folder guides |
| `assests/` | Project poster, logos, and banners |
| `data/` | Source documents used by the chatbot |
| `db/` | Persisted vector database (ChromaDB) |
| `notes/` | Architecture and technical notes (this file) |

### Files

| File | Purpose |
|---|---|
| `app.py` | Runs the Flask web app and exposes chat endpoints |
| `chat.py` | Handles the chat flow between user and model |
| `main.py` | Main entry point of the project |
| `make_image.py` | Generates image files for the data folder |
| `make_pdf.py` | Generates PDF files for the data folder |
| `multimodal.py` | Processes text and images together |
| `query.py` | Retrieves relevant chunks from ChromaDB for a query |