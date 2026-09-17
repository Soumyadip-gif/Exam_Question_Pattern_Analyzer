from processing.pattern_analyzer import analyze_topic_frequency


questions = [
    {"topic": "DBMS"},
    {"topic": "DBMS"},
    {"topic": "Java"},
    {"topic": "Operating System"},
    {"topic": "DBMS"},
    {"topic": "Java"}
]


result = analyze_topic_frequency(questions)

print("Topic Frequency:")
print(result)