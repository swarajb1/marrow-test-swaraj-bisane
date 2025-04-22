import os
from uuid import uuid4

import fitz  # PyMuPDF


def save_text_to_pdf(text: str, filename: str | None = None) -> str:
    try:
        filename = str(uuid4()) + ".pdf" if filename is None else filename

        doc = fitz.open()  # new PDF
        page = doc.new_page()
        page.insert_text((72, 72), text, fontsize=12)
        doc.save(os.path.join("created_files", filename))
        doc.close()

        return filename

    except Exception as e:
        raise OSError("Failed to save PDF: " + str(e))
