import streamlit as st
from PyPDF2 import PdfReader
from typing import List
from pydantic import BaseModel, Field
import asyncio
import json # Import json for debugging potentially malformed JSON

# Correctly import the necessary components from the agents library
from agents import Agent, Runner
# Import the model configuration from myconfig.py
from myconfig import MODEL, GEMINI_API_KEY

# 1. Configuration & API Key Setup
if not GEMINI_API_KEY:
    st.error("🚨 GEMINI_API_KEY not found! Please ensure it is set in your .env file.")
    st.stop()

# 2. Pydantic Schemas for Structured Output
class Question(BaseModel):
    """A single multiple-choice question with options and a correct answer."""
    question_text: str = Field(description="The text of the question.")
    options: List[str] = Field(description="A list of 4-5 multiple-choice options.")
    correct_answer: str = Field(description="The exact text of the correct option.")

class QuizQuestions(BaseModel):
    """A list of multiple-choice questions based on the provided text."""
    questions: List[Question] = Field(description="A list of quiz questions.")

# 3. Tool Definition - REMOVED

# Asynchronous function to run the agent
async def run_agent_async(agent: Agent, prompt: str):
    """Helper function to run the agent asynchronously."""
    result = await Runner.run(agent, prompt)
    return result.final_output

# 4. Streamlit UI & Logic
st.set_page_config(layout="wide")
st.title("📚 AI-Powered Study Assistant: PDF Summarizer & Quiz Generator")

# Initialize session state
if "raw_text" not in st.session_state:
    st.session_state.raw_text = ""
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None
if "selected_answers" not in st.session_state:
    st.session_state.selected_answers = {}
if "show_results" not in st.session_state:
    st.session_state.show_results = False


# Initialize the Agent
# Using the model imported from myconfig.py
try:
    study_buddy_agent = Agent(
        name="StudyBuddy",
        instructions="You are an expert academic assistant. Your goal is to help users study by summarizing text or generating quizzes in JSON format.",
        model=MODEL, # Use the imported model
    )
except Exception as e:
    st.error(f"Failed to initialize the agent: {e}")
    st.stop()


# --- UI Columns ---
col1, col2 = st.columns(2)

with col1:
    st.header("1. Upload & Extract")
    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            try:
                reader = PdfReader(uploaded_file)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                st.session_state.raw_text = text
                st.success(f"Extracted {len(text.split())} words from the PDF.")
            except Exception as e:
                st.error(f"Failed to read PDF: {e}")

    if st.session_state.raw_text:
        with st.expander("View Extracted Text"):
            st.text_area("", st.session_state.raw_text, height=200)

with col2:
    if st.session_state.raw_text:
        st.header("2. Get a Summary")
        if st.button("Summarize Document"):
            with st.spinner("Generating summary..."):
                try:
                    prompt = f"Please provide a concise summary of the following text:\n\n---\n\n{st.session_state.raw_text}"
                    summary_text = asyncio.run(run_agent_async(study_buddy_agent, prompt))
                    st.session_state.summary = summary_text
                except Exception as e:
                    st.error(f"Failed to generate summary: {e}")

        if st.session_state.summary:
            st.subheader("Summary:")
            st.info(st.session_state.summary)

        st.header("3. Create a Quiz")
        if st.button("Create Quiz"):
            st.session_state.quiz_data = None # Reset previous quiz
            st.session_state.selected_answers = {}
            st.session_state.show_results = False
            with st.spinner("Generating quiz... this may take a moment."):
                # Define the schema as a string for the prompt
                schema_string = json.dumps(QuizQuestions.model_json_schema(), indent=2)
                
                # Create a detailed prompt asking for JSON output
                json_prompt = f"""
                Based on the following text, generate a quiz with 5 multiple-choice questions.
                Your response MUST be ONLY the JSON object that conforms to the following JSON schema.
                Do not include any other text, explanations, or markdown formatting like ```json.

                JSON Schema:
                {schema_string}

                Text to analyze:
                ---
                {st.session_state.raw_text}
                ---
                """
                
                try:
                    # Call the main agent with the specific JSON prompt
                    json_output = asyncio.run(run_agent_async(study_buddy_agent, json_prompt))
                    
                    # Manually parse the JSON output
                    quiz_result = QuizQuestions.model_validate_json(json_output)
                    st.session_state.quiz_data = quiz_result

                except Exception as e:
                    st.error(f"Failed to create or parse quiz: {e}")
                    st.write("Agent output might not be valid JSON.")
                    st.write("Raw agent output for debugging:", json_output)

                    
# --- Display Quiz Below Columns ---
if st.session_state.quiz_data:
    st.header("Quiz Time!")
    st.write("Test your knowledge based on the document.")

    for i, q in enumerate(st.session_state.quiz_data.questions):
        st.subheader(f"Question {i + 1}: {q.question_text}")
        # Radio buttons for options
        user_answer = st.radio(
            f"Options for Question {i+1}",
            options=q.options,
            key=f"q_{i}",
            label_visibility="collapsed"
        )
        st.session_state.selected_answers[i] = user_answer

    if st.button("Submit & See Results"):
        st.session_state.show_results = True

    if st.session_state.show_results:
        st.header("Quiz Results")
        correct_count = 0
        for i, q in enumerate(st.session_state.quiz_data.questions):
            user_ans = st.session_state.selected_answers.get(i)
            correct_ans = q.correct_answer

            if user_ans == correct_ans:
                correct_count += 1
                st.success(f"**Q{i+1}: {q.question_text}**\n\nYour answer: '{user_ans}' is correct! ✅")
            else:
                st.error(f"**Q{i+1}: {q.question_text}**\n\nYour answer: '{user_ans}'.\n\nCorrect answer: '{correct_ans}' ❌")
        st.subheader(f"You scored {correct_count} out of {len(st.session_state.quiz_data.questions)}.")