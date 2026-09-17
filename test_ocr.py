from processing.image_ocr import extract_text_from_image


image_path = "test_question_paper.png"

text = extract_text_from_image(image_path)

print("Extracted Text:")
print(text)