import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Download required NLTK resources
# nltk.download("punkt")
# nltk.download("punkt_tab")
# nltk.download("stopwords")


def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def process_question(question):

    cleaned_text = clean_text(question)

    tokens = word_tokenize(cleaned_text)

    stop_words = set(stopwords.words("english"))

    keywords = [
        word for word in tokens
        if word not in stop_words and len(word) > 2
    ]

    return {
        "original": question,
        "cleaned": cleaned_text,
        "keywords": keywords
    }