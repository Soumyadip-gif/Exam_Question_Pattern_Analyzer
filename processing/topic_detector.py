# Topic keywords
TOPIC_KEYWORDS = {

    "DBMS": [
        "database",
        "dbms",
        "sql",
        "normalization",
        "transaction",
        "primary key",
        "foreign key",
        "relational",
        "er diagram",
        "query",
        "table",
        "schema"
    ],

    "Operating System": [
        "operating system",
        "process",
        "process scheduling",
        "deadlock",
        "memory management",
        "paging",
        "segmentation",
        "thread",
        "cpu scheduling",
        "virtual memory"
    ],

    "Java": [
        "java",
        "class",
        "object",
        "inheritance",
        "polymorphism",
        "encapsulation",
        "constructor",
        "interface",
        "exception",
        "multithreading"
    ],

    "Software Engineering": [
        "software engineering",
        "sdlc",
        "waterfall",
        "agile",
        "software testing",
        "requirement",
        "software design",
        "maintenance",
        "verification",
        "validation"
    ],

    "Computer Network": [
        "computer network",
        "network",
        "tcp",
        "ip",
        "udp",
        "http",
        "ftp",
        "osi",
        "router",
        "switch",
        "topology"
    ],

    "Data Structure": [
        "data structure",
        "array",
        "linked list",
        "stack",
        "queue",
        "tree",
        "graph",
        "sorting",
        "searching",
        "binary search"
    ]
}


def detect_topic(question):

    question = question.lower()

    topic_scores = {}

    for topic, keywords in TOPIC_KEYWORDS.items():

        score = 0

        for keyword in keywords:

            if keyword in question:
                score += 1

        topic_scores[topic] = score

    best_topic = max(topic_scores, key=topic_scores.get)

    if topic_scores[best_topic] == 0:
        return "General / Unknown"

    return best_topic