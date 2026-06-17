import streamlit as st

from modules.chatbot import chat_with_ai
from modules.flashcard_generator import generate_flashcards
from modules.pdf_reader import extract_pdf_text
from modules.quiz_generator import generate_quiz
from modules.summarizer import summarize_text
from modules.topic_explainer import explain_topic


st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="wide",
)


st.markdown(
    """
    <style>
    .main-header {
        padding: 1.4rem 1.6rem;
        border-radius: 14px;
        background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 58%, #06b6d4 100%);
        color: white;
        margin-bottom: 1.2rem;
    }
    .main-header h1 { margin: 0; font-size: 2.4rem; }
    .main-header p { margin: .4rem 0 0 0; font-size: 1.05rem; color: #dbeafe; }
    .feature-card {
        padding: 1rem;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        background: #ffffff;
        min-height: 118px;
    }
    .answer-box {
        padding: 1rem;
        border-left: 5px solid #2563eb;
        border-radius: 10px;
        background: #f8fafc;
        margin-top: .7rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def show_header():
    st.markdown(
        """
        <div class="main-header">
            <h1>AI-Powered Study Buddy</h1>
            <p>Explain topics, summarize notes, generate quizzes, create flashcards, and ask doubts in one place.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def get_notes_input(pdf_text):
    if pdf_text:
        return pdf_text

    return st.text_area(
        "Paste your notes here",
        height=240,
        placeholder="Example: Artificial Intelligence is the ability of machines to perform tasks that usually require human intelligence...",
    )


def render_quiz(quiz):

    if isinstance(quiz, str):

        st.markdown(quiz)
        return


    for index, item in enumerate(quiz, start=1):

        with st.expander(
            f"{index}. {item.get('Question','Question')}"
        ):

            st.write("Options:")

            options = item.get("Options", [])

            for option in options:
                st.write(option)


            st.success(
                f"Correct Answer: {item.get('Answer','Not available')}"
            )


            explanation = item.get("Explanation")

            if explanation:
                st.info(explanation)


def render_flashcards(cards):

    if isinstance(cards, str):

        st.markdown(cards)
        return


    for index, card in enumerate(cards, start=1):

        with st.container(border=True):

            st.markdown(
                f"**Card {index}: {card.get('Question', 'Question')}**"
            )

            st.write(
                card.get("Answer", "Answer not available")
            )


def render_response(response):
    with st.container(border=True):
        st.markdown(response)


show_header()

with st.sidebar:
    st.title("Study Buddy")
    menu = st.radio(
        "Choose a feature",
        [
            "Dashboard",
            "Topic Explainer",
            "Summarizer",
            "Quiz Generator",
            "Flashcards",
            "AI Tutor",
        ],
    )
    st.divider()
    st.caption("For Gemini responses, set GEMINI_API_KEY in environment variables or Streamlit secrets.")


uploaded_file = st.file_uploader("Upload PDF study material", type=["pdf"])
pdf_text = ""

if uploaded_file:
    with st.spinner("Reading PDF..."):
        pdf_text = extract_pdf_text(uploaded_file)

    if pdf_text:
        st.success("PDF uploaded and text extracted successfully.")
        with st.expander("Preview extracted text"):
            st.write(pdf_text[:5000])
    else:
        st.warning("No readable text was found in the PDF. Try another PDF or paste notes manually.")


if menu == "Dashboard":
    st.subheader("Project Demo Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.subheader("Topic Explainer")
            st.write("Explains any topic by learning level to make it easier.")

    with col2:
        with st.container(border=True):
            st.subheader("Notes Summarizer")
            st.write("Converts long notes into short summaries and key points.")

    with col3:
        with st.container(border=True):
            st.subheader("Practice Tools")
            st.write("Creates quizzes and flashcards from notes or PDFs.")

    st.info("Demo flow: upload or paste study material, generate a summary, create quiz questions, then ask the AI Tutor a doubt.")

elif menu == "Topic Explainer":
    st.subheader("Topic Explainer")
    col1, col2 = st.columns([2, 1])
    with col1:
        topic = st.text_input("Enter topic", placeholder="Example: Photosynthesis, DBMS normalization, Machine Learning")
    with col2:
        level = st.selectbox("Learning level", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Explain Topic", type="primary"):
        if not topic.strip():
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Preparing explanation..."):
                response = explain_topic(topic.strip(), level)
            render_response(response)

elif menu == "Summarizer":
    st.subheader("Notes Summarizer")
    notes = get_notes_input(pdf_text)

    if st.button("Summarize", type="primary"):
        if not notes.strip():
            st.warning("Please upload a PDF or paste notes.")
        else:
            with st.spinner("Summarizing notes..."):
                summary = summarize_text(notes)
            render_response(summary)

elif menu == "Quiz Generator":
    st.subheader("Quiz Generator")
    notes = get_notes_input(pdf_text)

    if st.button("Generate Quiz", type="primary"):
        if not notes.strip():
            st.warning("Please upload a PDF or paste notes.")
        else:
            with st.spinner("Creating quiz..."):
                quiz = generate_quiz(notes)
            render_quiz(quiz)

elif menu == "Flashcards":
    st.subheader("Flashcard Generator")
    notes = get_notes_input(pdf_text)

    if st.button("Generate Flashcards", type="primary"):
        if not notes.strip():
            st.warning("Please upload a PDF or paste notes.")
        else:
            with st.spinner("Creating flashcards..."):
                cards = generate_flashcards(notes)
            render_flashcards(cards)

elif menu == "AI Tutor":
    st.subheader("AI Tutor")
    question = st.text_area(
        "Ask your question",
        height=140,
        placeholder="Example: Explain overfitting in machine learning with an example.",
    )

    if st.button("Ask AI Tutor", type="primary"):
        if not question.strip():
            st.warning("Please enter your question.")
        else:
            with st.spinner("Thinking..."):
                response = chat_with_ai(question.strip())
            render_response(response)