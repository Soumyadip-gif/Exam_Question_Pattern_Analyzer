from processing.topic_detector import detect_topic


questions = [
    "What is normalization in DBMS?",
    "Explain process scheduling.",
    "What is inheritance in Java?",
    "Explain SDLC models.",
    "What is TCP and UDP?",
    "Explain linked list."
]


for question in questions:

    topic = detect_topic(question)

    print("Question:", question)
    print("Topic:", topic)
    print("-" * 50)