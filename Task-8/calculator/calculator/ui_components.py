import streamlit as st

def create_button(label, key, on_click_callback, use_container_width=True):
    st.button(label, key=key, on_click=on_click_callback, args=(label,), use_container_width=use_container_width)

def create_calculator_grid(on_button_click):
    buttons = [
        ['C', '(', ')', '\u00F7'],
        ['7', '8', '9', '\u00D7'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '.', '=', 'DEL'],
    ]

    for row_buttons in buttons:
        cols = st.columns(len(row_buttons))
        for i, button_label in enumerate(row_buttons):
            with cols[i]:
                if button_label == '=':
                    st.button(button_label, key=f"btn_{button_label}", on_click=on_button_click, args=('=',), use_container_width=True)
                elif button_label == 'C':
                    st.button(button_label, key=f"btn_{button_label}", on_click=on_button_click, args=('C',), use_container_width=True)
                elif button_label == 'DEL':
                    st.button(button_label, key=f"btn_{button_label}", on_click=on_button_click, args=('DEL',), use_container_width=True)
                else:
                    st.button(button_label, key=f"btn_{button_label}", on_click=on_button_click, args=(button_label,), use_container_width=True)
