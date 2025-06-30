import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

os.environ["TESSDATA_PREFIX"] = r"C:/Program Files/Tesseract-OCR/tessdata/"

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
