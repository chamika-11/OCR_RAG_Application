import streamlit as st
import os
from PIL import Image
from ocr_engine import extract_text
from preprocess import preprocess_image
from extract import extract_structured_data
from rag_chatbot import ask_question
from classifier import predict_document_type
from utils import convert_pdf_to_images
from torchvision.datasets import ImageFolder


# Load class labels once
dataset = ImageFolder("data/classification")
class_labels = dataset.classes

st.set_page_config(page_title="Smart OCR System", layout="wide")
st.title("📄 Smart Document OCR + Chatbot")

uploaded_file = st.file_uploader("Upload a document (PDF or Image)", type=["pdf", "jpg", "png", "jpeg"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    if file_ext == "pdf":
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        image_paths = convert_pdf_to_images("temp.pdf")
    else:
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.read())
        image_paths = ["temp.jpg"]

    full_text = ""
    structured_data = []
    document_types = []

    for path in image_paths:
        processed = preprocess_image(path)
        text = extract_text(path)
        struct = extract_structured_data(text)
        doc_type = predict_document_type(path, class_labels=class_labels)

        full_text += text + "\n"
        structured_data.append(struct)
        document_types.append(doc_type)

    st.success("✅ OCR and Classification Complete!")

    # Display document classification and structured data
    st.subheader("📌 Document Type(s)")
    st.write(list(set(document_types)))

    st.subheader("🧾 Structured Data")
    st.json(structured_data)

    st.subheader("📝 Raw OCR Text")
    st.text_area("Text", value=full_text, height=300)

    # Chatbot
    st.subheader("🤖 Ask a Question")
    question = st.text_input("Ask about this document:")

    if st.button("Get Answer") and question:
        answer = ask_question(full_text, question)
        st.success(answer)
