import re


def extract_questions(text):
    """
    Extract individual questions from normal PDF text or OCR text.

    Supports:
    1.  What is PHP?
    2.  What is MySQL?
    Q1. What is PHP?
    Q2. What is MySQL?
    (i) What is PHP?
    (ii) What is MySQL?
    i) What is PHP?
    ii) What is MySQL?
    a) What is PHP?
    b) What is MySQL?

    Also handles questions appearing on the same line.
    """

    # =================================
    # STEP 1: NORMALIZE TEXT
    # =================================

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Replace multiple spaces/tabs with one space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n", text)

    text = text.strip()


    # =================================
    # STEP 2: REMOVE COMMON SECTION HEADINGS
    # =================================

    # These are not questions.
    text = re.sub(
        r"Group[-\s]*(?:A|B|C)\s*"
        r"\([^)]*Answer[^)]*\)",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"Group[-\s]*(?:A|B|C)"
        r"(?:\s*\([^)]*\))?",
        "",
        text,
        flags=re.IGNORECASE
    )


    # =================================
    # STEP 3: QUESTION MARKER PATTERN
    # =================================

    question_marker = re.compile(
        r"""
        (?:
            # Question 1 / Question 2
            \bQuestion\s*\d+\s*[\.\):\-]?

            |

            # Q1 / Q2
            \bQ\s*\d+\s*[\.\):\-]?

            |

            # Numbered questions: 1. / 2) / 3:
            (?<![\w])
            \d{1,2}\s*[\.\):\-]

            |

            # Roman questions: (i) / (ii) / (iii)
            \(\s*
            (?:i|ii|iii|iv|v|vi|vii|viii|ix|x)
            \s*\)

            |

            # Roman questions: i) / ii) / iii)
            (?<![\w])
            (?:i|ii|iii|iv|v|vi|vii|viii|ix|x)
            \s*[\)\.:]

            |

            # Alphabetic questions: a) / b) / c)
            (?<![\w])
            [a-h]
            \s*[\)\.:]
        )
        """,
        re.IGNORECASE | re.VERBOSE
    )


    # =================================
    # STEP 4: FIND QUESTION POSITIONS
    # =================================

    matches = list(question_marker.finditer(text))

    questions = []

    if not matches:
        return questions


    # =================================
    # STEP 5: SPLIT INTO QUESTIONS
    # =================================

    for index, match in enumerate(matches):

        start = match.end()

        if index + 1 < len(matches):
            end = matches[index + 1].start()
        else:
            end = len(text)

        question_text = text[start:end].strip()


        # =================================
        # STEP 6: CLEAN QUESTION TEXT
        # =================================

        # Remove unwanted leading punctuation
        question_text = re.sub(
            r"^[\s\-\:\.\)]+",
            "",
            question_text
        )

        # Remove section headings that may appear
        # at the end of OCR text
        question_text = re.split(
            r"\bGroup[-\s]*(?:A|B|C)\b",
            question_text,
            maxsplit=1,
            flags=re.IGNORECASE
        )[0].strip()


        # =================================
        # STEP 7: IGNORE VERY SHORT TEXT
        # =================================

        if len(question_text) < 8:
            continue


        # =================================
        # STEP 8: ADD QUESTION
        # =================================

        questions.append(question_text)


    return questions