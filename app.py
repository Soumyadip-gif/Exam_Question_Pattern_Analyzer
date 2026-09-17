from flask import Flask, render_template, request, redirect, url_for
import os

from processing.pdf_extractor import (
    extract_text_from_pdf,
    extract_text_from_pdf_ocr
)

from processing.question_extractor import extract_questions
from processing.nlp_processor import process_question
from processing.topic_detector import detect_topic
from processing.similarity_analyzer import calculate_similarity

from processing.pattern_analyzer import (
    analyze_topic_frequency,
    get_important_topics,
    generate_pattern_insights,
    find_frequently_asked_questions
)

from processing.image_ocr import extract_text_from_image
from PIL import Image


app = Flask(__name__)


UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    if "question_paper" not in request.files:
        return "No file selected."

    file = request.files["question_paper"]

    if file.filename == "":
        return "No file selected."

    if not allowed_file(file.filename):
        return "Only PDF, JPG, JPEG, and PNG files are allowed."

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(file_path)


    # =================================
    # EXTRACT TEXT
    # =================================

    file_extension = file.filename.rsplit(".", 1)[1].lower()


    if file_extension == "pdf":

        extracted_text = extract_text_from_pdf(file_path)

        # OCR fallback for scanned PDFs
        if len(extracted_text.strip()) < 100:

            print("Little or no text detected. Starting OCR...")

            extracted_text = extract_text_from_pdf_ocr(file_path)


    else:

        print("Image detected. Starting OCR...")

        image = Image.open(file_path)

        extracted_text = extract_text_from_image(file_path)


    # =================================
    # EXTRACT QUESTIONS
    # =================================

    questions = extract_questions(extracted_text)

    processed_questions = []


    # =================================
    # NLP + TOPIC DETECTION
    # =================================

    for question in questions:

        result = process_question(question)

        result["topic"] = detect_topic(question)

        processed_questions.append(result)


    # =================================
    # SIMILARITY ANALYSIS
    # =================================

    similarity_matrix = calculate_similarity(
        processed_questions
    )

    similar_questions = []

    similarity_threshold = 0.50


    for i in range(len(processed_questions)):

        for j in range(i + 1, len(processed_questions)):

            score = similarity_matrix[i][j]

            if score >= similarity_threshold:

                similar_questions.append({
                    "question1": i + 1,
                    "question2": j + 1,
                    "score": round(float(score), 2)
                })


    # =================================
    # TOPIC FREQUENCY
    # =================================

    topic_frequency = analyze_topic_frequency(
        processed_questions
    )


    # =================================
    # IMPORTANT TOPICS
    # =================================

    important_topics = get_important_topics(
        topic_frequency
    )


    # =================================
    # PATTERN INSIGHTS
    # =================================

    pattern_insights = generate_pattern_insights(
        processed_questions,
        topic_frequency,
        similar_questions
    )


    # =================================
    # FREQUENTLY ASKED QUESTIONS
    # =================================

    frequently_asked = find_frequently_asked_questions(
        processed_questions,
        similar_questions
    )


    # =================================
    # DISPLAY RESULTS
    # =================================

    return render_template(
        "results.html",

        questions=processed_questions,

        similar_questions=similar_questions,

        topic_frequency=topic_frequency,

        important_topics=important_topics,

        pattern_insights=pattern_insights,

        frequently_asked=frequently_asked
    )


if __name__ == "__main__":
    app.run(debug=True)