import fitz  # PyMuPDF
from typing import List, Dict

def extract_pages(pdf_path: str) -> List[Dict]:
    """
    Extract text page by page with metadata.
    Returns list of {page_num, text}
    """

    doc = fitz.open(pdf_path)
    pages = []

    for i, page in enumerate(doc):
        text = page.get_text("text")

        if not text.strip():
            continue

        pages.append({
            "page": i + 1,
            "text": text
        })

    return pages
