import pytesseract

from PIL import Image, ImageEnhance, ImageFilter, ImageOps


# =================================
# TESSERACT INSTALLATION PATH
# =================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# =================================
# IMAGE PREPROCESSING
# =================================

def preprocess_image(image):
    """
    Prepare an image before OCR.
    """

    # Make sure image is RGB
    image = image.convert("RGB")


    # =================================
    # 1. ENLARGE IMAGE
    # =================================

    width, height = image.size

    image = image.resize(
        (width * 2, height * 2),
        Image.Resampling.LANCZOS
    )


    # =================================
    # 2. GRAYSCALE
    # =================================

    image = ImageOps.grayscale(image)


    # =================================
    # 3. IMPROVE CONTRAST
    # =================================

    image = ImageEnhance.Contrast(image).enhance(2.0)


    # =================================
    # 4. SHARPEN
    # =================================

    image = image.filter(
        ImageFilter.SHARPEN
    )


    # =================================
    # 5. THRESHOLD
    # =================================

    image = image.point(
        lambda pixel: 0 if pixel < 180 else 255
    )


    return image


# =================================
# OCR FUNCTION
# =================================

def extract_text_from_image(image):
    """
    Extract text from an image using Tesseract OCR.

    Accepts:
    - PIL Image
    - Image file path
    """

    # =================================
    # CHECK IF INPUT IS A FILE PATH
    # =================================

    if isinstance(image, str):

        image = Image.open(image)


    # =================================
    # PREPROCESS IMAGE
    # =================================

    processed_image = preprocess_image(image)


    # =================================
    # TESSERACT CONFIGURATION
    # =================================

    custom_config = (
        "--oem 3 "
        "--psm 6"
    )


    # =================================
    # EXTRACT TEXT
    # =================================

    extracted_text = pytesseract.image_to_string(
        processed_image,
        config=custom_config,
        lang="eng"
    )


    # =================================
    # BASIC TEXT CLEANING
    # =================================

    extracted_text = extracted_text.replace(
        "\r\n",
        "\n"
    )

    extracted_text = extracted_text.replace(
        "\r",
        "\n"
    )


    return extracted_text