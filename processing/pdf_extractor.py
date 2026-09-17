import pymupdf
from PIL import Image


def extract_text_from_pdf(pdf_path):
    """
    Extract selectable text from a normal PDF.
    """

    document = pymupdf.open(pdf_path)

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()

    return extracted_text


def extract_text_from_pdf_ocr(pdf_path):
    """
    Convert PDF pages into images and extract text using OCR.
    """

    from processing.image_ocr import extract_text_from_image

    document = pymupdf.open(pdf_path)

    extracted_text = ""

    for page in document:

        # Render PDF page as an image
        pixmap = page.get_pixmap(
            matrix=pymupdf.Matrix(2, 2)
        )

        # Convert Pixmap to PIL Image
        image = Image.frombytes(
            "RGB",
            [pixmap.width, pixmap.height],
            pixmap.samples
        )

        # Extract text using Tesseract
        page_text = extract_text_from_image(image)

        extracted_text += page_text + "\n"

    document.close()

    return extracted_text