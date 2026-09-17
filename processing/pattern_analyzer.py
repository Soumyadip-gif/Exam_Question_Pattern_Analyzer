from collections import Counter


def analyze_topic_frequency(questions):
    topics = []

    for question in questions:
        topics.append(question["topic"])

    topic_frequency = Counter(topics)

    return dict(topic_frequency)


def get_important_topics(topic_frequency):
    """
    Return topics sorted by frequency.
    """

    important_topics = sorted(
        topic_frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return important_topics

def generate_pattern_insights(questions, topic_frequency, similar_questions):
    """
    Generate basic pattern insights from the analyzed question paper.
    """

    total_questions = len(questions)

    # Find the most frequently asked topic
    if topic_frequency:
        most_asked_topic = max(
            topic_frequency,
            key=topic_frequency.get
        )

        most_asked_topic_count = topic_frequency[
            most_asked_topic
        ]
    else:
        most_asked_topic = "None"
        most_asked_topic_count = 0

    # Number of detected topics
    topics_detected = len(topic_frequency)

    # Number of similar/repeated question pairs
    repeated_questions = len(similar_questions)

    return {
        "total_questions": total_questions,
        "most_asked_topic": most_asked_topic,
        "most_asked_topic_count": most_asked_topic_count,
        "topics_detected": topics_detected,
        "repeated_questions": repeated_questions
    }

def find_frequently_asked_questions(questions, similar_questions):
    """
    Find questions that appear repeatedly or have
    high similarity with other questions.
    """

    frequency = {}

    for item in similar_questions:

        question1 = item["question1"]
        question2 = item["question2"]

        score = item["score"]

        # Count both questions
        frequency[question1] = frequency.get(question1, 0) + 1
        frequency[question2] = frequency.get(question2, 0) + 1

    frequently_asked = []

    for question_number, count in frequency.items():

        if question_number <= len(questions):

            frequently_asked.append({
                "question_number": question_number,
                "question": questions[question_number - 1]["original"],
                "frequency": count
            })

    # Highest frequency first
    frequently_asked.sort(
        key=lambda x: x["frequency"],
        reverse=True
    )

    return frequently_asked