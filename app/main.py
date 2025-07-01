from fastapi import FastAPI, UploadFile, File, Form
from ocr_engine import extract_text
from classifier import train_document_classifier
from classifier import predict_document_type
from torchvision.datasets import ImageFolder
from extract import extract_structured_data
from rag_chatbot import ask_question
from pdf2image import convert_from_bytes
from PIL import Image
import os

app = FastAPI()

# Prepare class labels at startup
dataset = ImageFolder("data/classification")
class_labels = dataset.classes

# Temporary memory
doc_store = {
    "ocr_text": None,
    "structured_data": None,
    "document_type": None
}

@app.post("/upload-document/")
async def upload_document(file: UploadFile = File(...)):
    file_bytes=await file.read()

    if file.filename.lower().endswith(".pdf"):
        images=convert_from_bytes(file_bytes,poppler_path="C:/Program Files/poppler-24.08.0/Library/bin")
        images[0].save("uploaded.jpg","JPEG")
    else:
        with open("uploaded.jpg","wb") as f:
            f.write(file_bytes)

    train_document_classifier()

    text = extract_text("uploaded.jpg")
    structured_data = extract_structured_data(text)
    doc_type = predict_document_type("uploaded.jpg", class_labels=class_labels)
    #store results
    doc_store["ocr_text"] = text
    doc_store["structured_data"] = structured_data
    doc_store["document_type"] = doc_type

    return {
        "message": "Document uploaded, OCR and classification successful.",
        "document_type": doc_type,
        "extracted_text": text,
        "structured_data": structured_data
    }

@app.post("/chat/")
async def chat_bot(question: str = Form(...)):
    if doc_store["ocr_text"] is None:
        return {"error": "No document has been uploaded yet."}

    answer = ask_question(doc_store["ocr_text"], question)
    return {
        "document_type": doc_store["document_type"],
        "answer": answer
    }
