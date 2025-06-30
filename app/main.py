from fastapi import FastAPI, UploadFile, File
from ocr_engine import extract_text
from classifier import predict_document_type
from torchvision.datasets import ImageFolder
from extract import extract_structured_data
from rag_chatbot import ask_question
from fastapi import Form

app = FastAPI()

#prepare class labels at startup
dataset=ImageFolder("data/classification")
class_labels=dataset.classes

@app.post("/ocr/")
async def ocr_chat(file: UploadFile = File(...), question: str = Form(...)):
    with open("sampleText.jpg", "wb") as f:
        f.write(await file.read())

    text = extract_text("sampleText.jpg")
    structured_data = extract_structured_data(text)
    doc_type = predict_document_type("sampleText.jpg", class_labels=class_labels)
    answer = ask_question(text, question)

    return {"document_type": doc_type,
    "extracted_text": text,
    "structured_data": structured_data,"answer": answer}
