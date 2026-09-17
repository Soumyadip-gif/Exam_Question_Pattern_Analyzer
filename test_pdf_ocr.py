from processing.pdf_extractor import extract_text_from_pdf_ocr


pdf_path = r"C:\Users\HP\Documents\Project files\Exam-Question-Pattern-Analyzer\test_question_paper.pdf"

text = extract_text_from_pdf_ocr(pdf_path)

print("\n===== OCR EXTRACTED TEXT =====\n")
print(text)