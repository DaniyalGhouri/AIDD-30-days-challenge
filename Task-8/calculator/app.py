import streamlit as st
from calculator.calculator_logic import add_value, evaluate_expression, clear_expression, backspace_delete
from calculator.ui_components import create_calculator_grid

# Initialize session state
if 'expression' not in st.session_state:
    st.session_state.expression = ""
if 'display' not in st.session_state:
    st.session_state.display = "0"

# --- Styling (Dark Theme) ---
st.markdown("""
<style>
.main .block-container {
    background-color: #262626; /* Dark background */
    color: white;
}
.stButton>button {
    background-color: #404040;
    color: white !important;
    border-radius: 5px;
    border: 1px solid #555555;
    font-size: 20px;
    height: 60px;
    margin: 5px;
    line-height: 1; /* Ensure text is vertically centered */
    font-family: monospace !important; /* Explicitly set font */
}
.stButton>button:hover {
    background-color: #595959;
}
.stTextInput>div>div>input {
    background-color: #333333;
    color: white !important; /* Ensure text color is white */
    font-size: 3em;
    text-align: right;
    border: none;
    padding: 10px;
    height: 150px !important;
    line-height: 1.2; /* Adjust line height for better vertical alignment */
    font-family: monospace !important; /* Explicitly set font */
}

/* Specific styling for + and - buttons */
div[data-testid="stButton"] > button[key="btn_+"] {
    color: white !important;
    font-weight: bolder !important;
}
div[data-testid="stButton"] > button[key="btn_-"] {
    color: white !important;
    font-weight: bolder !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Streamlit Calculator")

# Debug display for expression (temporary)

# Display panel
st.markdown(f"""
<div style="
    background:#333333;
    padding:20px;
    width:100%;
    text-align:right;
    font-size:48px;
    border-radius:8px;
    color:white;
    font-family:monospace;
    border:1px solid #444;
">
{st.session_state.display}
</div>
""", unsafe_allow_html=True)

# Callback for button clicks
def on_button_click(label):
    if label.isdigit() or label == '.':
        st.session_state.expression = add_value(st.session_state.expression, label)
        st.session_state.display = st.session_state.expression
    elif label in ['+', '-', '\u00D7', '\u00F7']:
        st.session_state.expression = add_value(st.session_state.expression, label)
        st.session_state.display = st.session_state.expression
    elif label == '=':
        result = evaluate_expression(st.session_state.expression)
        st.session_state.display = result
        st.session_state.expression = result if result != "Error" else ""
    elif label == 'C':
        st.session_state.expression, st.session_state.display = clear_expression()
    elif label == 'DEL':
        st.session_state.expression, st.session_state.display = backspace_delete(st.session_state.expression, st.session_state.display)


# Create button grid
# Minor edit to trigger Streamlit rerun
create_calculator_grid(on_button_click)
