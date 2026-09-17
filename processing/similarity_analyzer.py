from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(questions):

    if len(questions) < 2:
        return []

    # Extract question text
    texts = [question["cleaned"] for question in questions]

    # Convert questions into TF-IDF vectors
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(texts)

    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix