from gemini_helper import ask_gemini


def explain_topic(topic, level):

    prompt = f"""

You are an expert AI teacher.

Explain the topic: {topic}

Target student level:
{level}


Provide the explanation in this format:


## Definition
Explain the concept clearly.


## Simple Explanation
Explain in easy student-friendly language.


## How It Works
Explain step-by-step.


## Architecture / Process
Explain the flow if applicable.


## Real World Applications
Give practical examples.


## Advantages


## Limitations


## Important Exam Points


## Interview Questions


Use simple English.
Avoid unnecessary complexity.

"""


    try:
        response = ask_gemini(prompt)
        if response:
            return response


    except Exception as e:
        return f"Gemini Error: {e}"

    return """
Gemini is currently unavailable.

Please configure your API key.
"""