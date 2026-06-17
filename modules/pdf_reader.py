from PyPDF2 import PdfReader


def extract_pdf_text(pdf_file):
    reader = PdfReader(pdf_file)
    pages = []

    for page in reader.pages:
        page_text = page.extract_text() or ""
        if page_text.strip():
            pages.append(page_text.strip())

    return "\n\n".join(pages)