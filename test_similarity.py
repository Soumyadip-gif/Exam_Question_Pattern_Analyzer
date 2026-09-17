from processing.similarity_analyzer import calculate_similarity


questions = [
    {
        "cleaned": "what is database normalization"
    },
    {
        "cleaned": "explain database normalization"
    },
    {
        "cleaned": "what is primary key"
    },
    {
        "cleaned": "explain primary key in database"
    }
]


similarity_matrix = calculate_similarity(questions)


print("Similarity Matrix:")
print(similarity_matrix)


print("\nPairwise Similarity:")

for i in range(len(questions)):

    for j in range(i + 1, len(questions)):

        score = similarity_matrix[i][j]

        print(
            f"Question {i + 1} ↔ Question {j + 1}: "
            f"{score:.2f}"
        )