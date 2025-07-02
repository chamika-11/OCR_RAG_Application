# 🧠 Advanced OCR + RAG Document Intelligence System

This project is a real-world, production-ready OCR pipeline combined with a Retrieval-Augmented Generation (RAG) chatbot interface. It allows companies (e.g., banks, insurance firms) to upload customer-related documents like salary sheets, loan records, and IDs in PDF or image format. The system performs full OCR, extracts structured data, stores it, and enables natural language Q&A on the stored content using LLMs.

---

## 🚀 Features

- 🔁 **Batch Upload**: Upload multiple documents (PDFs/images) at once.
- 🖨️ **Multi-page PDF OCR**: Automatically converts and extracts text from all pages.
- 🧠 **Document Classification**: Classifies document type using AI.
- 📊 **Structured Data Extraction**: Extracts key fields (e.g., name, salary, loan amount).
- 💾 **Persistent JSON Storage**: Saves OCR results and extracted data permanently.
- 💬 **RAG Chatbot**: Ask natural language questions and get intelligent answers from uploaded documents.
- 🌐 **FastAPI Backend + Angular Frontend (in progress)**

---

## 🏗️ Tech Stack

- **Backend**: Python, FastAPI
- **OCR Engine**: Tesseract + OpenCV + PDF2Image
- **Structured Extraction**: Regex + Custom NLP rules
- **Document Classification**: PyTorch + torchvision
- **LLM-based Q&A**: Retrieval-Augmented Generation (RAG)
- **Frontend**: Angular (WIP)
- **Storage**: Local JSON files (can be upgraded to database)

---

## 📂 Example Use Case

> 💼 A bank uploads a folder of teacher salary slips, loan records, and income statements.  
> The system automatically:
> - Performs OCR on each file
> - Extracts key information (Name, Amount, Month)
> - Classifies document types
> - Stores the data as structured JSON
> ✅ Later, staff can ask: _"What is the total salary paid in June?"_ or _"Show me all customers with loans over Rs. 100,000."_ and get real answers powered by AI.


## 📝 To Do
 Multi-file, multi-page OCR

 Document classification

 Structured data extraction

 JSON storage

 RAG Q&A interface

 Angular Frontend integration

 Azure Blob / DB storage upgrade

 Company-based document separation
---

## 🧪 How to Run

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the FastAPI app
uvicorn main:app --reload

