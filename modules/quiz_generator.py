import json
from gemini_helper import ask_gemini


def generate_quiz(text):

    prompt = f"""

Create 5 MCQ questions from the notes.

Return ONLY valid JSON.

Do not add markdown.
Do not add ```.

Format:

[
  {{
    "Question": "What is Artificial Intelligence?",
    "Options": [
        "A) Machine",
        "B) Human",
        "C) AI System",
        "D) Data"
    ],
    "Answer": "C) AI System",
    "Explanation": "AI allows machines to perform tasks requiring human intelligence."
  }}
]


Notes:

{text}

"""

    response = ask_gemini(prompt)


    try:
        quiz = json.loads(response)
        return quiz

    except Exception:
        return response