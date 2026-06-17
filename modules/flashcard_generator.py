from gemini_helper import ask_gemini
import json


def generate_flashcards(text):

    prompt=f"""

Create 5 educational flashcards.

Return only JSON.

Format:

[
 {{
 "Question":"Question here",
 "Answer":"Answer here"
 }}
]


Notes:

{text}

"""

    response = ask_gemini(prompt)

    try:
        return json.loads(response)

    except:
        return response