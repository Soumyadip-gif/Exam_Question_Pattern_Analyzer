from processing.nlp_processor import process_question


question = "What is Database Management System?"

result = process_question(question)

print("Original:")
print(result["original"])

print("\nCleaned:")
print(result["cleaned"])

print("\nKeywords:")
print(result["keywords"])