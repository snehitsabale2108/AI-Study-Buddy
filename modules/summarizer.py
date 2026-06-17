from gemini_helper import ask_gemini


def summarize_text(text):
    if not text or not text.strip():
        return "Please provide notes to summarize."

    prompt = f"""
You are an AI study assistant.

Summarize the notes below for a student.

Return:
1. Short Summary
2. Important Points
3. Exam Revision Tips

Use simple English and clear bullet points.

Notes:
{text[:12000]}
"""

    response = ask_gemini(prompt)
    if response:
        return response

    sentences = [sentence.strip() for sentence in text.replace("\n", " ").split(".") if sentence.strip()]
    short = ". ".join(sentences[:3])
    points = "\n".join(f"- {sentence}" for sentence in sentences[:6])
    return f"Short Summary:\n{short}\n\nImportant Points:\n{points}"