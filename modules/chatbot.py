from gemini_helper import ask_gemini

def chat_with_ai(question):
    if not question or not question.strip():
        return "Please enter a question."

    prompt = f"""
You are a friendly AI tutor for students.

Answer the student question in simple English.
Use this structure:
1. Direct Answer
2. Step-by-Step Explanation
3. Easy Example
4. Quick Revision Point

Student question:
{question}
"""

    response = ask_gemini(prompt)
    return response or "I could not connect to Gemini. Please check your API key and internet connection."