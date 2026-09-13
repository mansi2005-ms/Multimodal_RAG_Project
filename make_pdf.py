from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

os.makedirs("data", exist_ok=True)
pdf_path = "data/sample.pdf"

doc = SimpleDocTemplate(pdf_path, pagesize=letter)
styles = getSampleStyleSheet()
story = [
    Paragraph("Multimodal RAG Chatbot Overview", styles['Title']),
    Paragraph("The Multimodal Retrieval-Augmented Generation (RAG) chatbot is an AI application designed to provide meaningful answers based on text documents, PDFs, and images[span_0](start_span)[span_0](end_span).", styles['Normal']),
    Paragraph("It uses LangChain to coordinate components, and ChromaDB as a vector database for storing and retrieving vector embeddings[span_1](start_span)[span_1](end_span).", styles['Normal'])
]
doc.build(story)
print("sample.pdf created successfully inside the data folder!")