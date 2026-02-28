from pypdf import PdfReader
import re


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    # Clean broken words and extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()