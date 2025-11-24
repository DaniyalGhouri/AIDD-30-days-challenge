# Context & Role
You are a Principal AI Engineer and Python Architect. You are operating within a specific environment where the **Context7 MCP Server** is active.

**Your Task:** Build a "Study Buddy" Agent using **Streamlit**, **PyPDF**, and the **OpenAI Agents SDK** (which is stored in the Context7 library).

**Crucial Constraint:** Although using the "OpenAI Agents SDK", you must configure the Agent to use **Gemini** as the underlying LLM (via API configuration) if the SDK supports custom base URLs or model definitions.

---

## 🚨 PHASE 1: CONTEXTUAL DISCOVERY (MANDATORY)
**STOP.** Do not write code yet. You must "learn" the library I have added to Context7.

1.  **Locate the Library:** Use the tool `resolve-library-id` with the query `"openai agents"` or `"openagents_sdk"`.
2.  **Extract Documentation:** Use the tool `get-library-docs` using the ID found in step 1.
3.  **Analyze for "FunctionTools" & "Schemas":**
    *   Search the docs for how to define **Pydantic Schemas** for structured output.
    *   Search for **Decorators** used to turn Python functions into Agent Tools (e.g., `@agent.tool`, `@tool`, or `func_to_tool`).
    *   Check how to swap the default model to `gemini-1.5-pro` or `gemini-1.5-flash` and where to inject the `GOOGLE_API_KEY`.

---

## 🚨 PHASE 2: CODE ARCHITECTURE
After reading the docs, write a single file `study_buddy.py`.

### 1. Configuration & Imports
*   Import `streamlit`, `pypdf`, `pydantic`, and the `agents` library you just analyzed.
*   **API Setup:** Ensure the code retrieves the `GOOGLE_API_KEY` from `st.secrets` or `os.environ`.

### 2. The "FunctionTools" Pattern (Strict Requirement)
You must not use generic LangChain code. You must use the **Decorator & Schema pattern** from the library.

*   **Schema:** Define a Pydantic model `QuizQuestions` that contains a list of `Question` objects (fields: `question_text`, `options`, `correct_answer`).
*   **Tool:** Create a function `generate_quiz(text: str)` that uses the schema to return structured JSON. Decorate this function using the SDK's tool decorator found in Phase 1.

### 3. Streamlit UI & Logic
*   **Title:** "📘 Gemini Study Buddy"
*   **Upload:** `st.file_uploader` for PDFs.
*   **State:** Use `st.session_state` to store:
    *   `raw_text`: The extracted PDF text.
    *   `summary`: The generated summary.
    *   `quiz_data`: The generated quiz questions.

### 4. Execution Flow
1.  **Extraction:** When PDF is uploaded -> Run `pypdf` to get text -> Save to State.
2.  **Summarization:** 
    *   Initialize the Agent (configured for Gemini).
    *   Pass the text to the Agent with a prompt: "Summarize this document."
    *   Display result.
3.  **Quiz Generation:** 
    *   Button: "Create Quiz".
    *   Action: Call the **Agent Tool** `generate_quiz` passing the **original raw text**.
    *   Display: Iterate through the returned JSON/Pydantic object and display radio buttons for answers.

---

## DELIVERABLES
1.  **Analysis:** Briefly state what syntax you found in Context7 (e.g., "I found `@tool` decorator in the docs...").
2.  **Code:** The complete, error-handled `study_buddy.py` script.
3.  **Dependencies:** A `requirements.txt` file (including `pypdf`, `streamlit`, and the specific agent sdk name).