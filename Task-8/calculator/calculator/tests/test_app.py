import pytest
from unittest.mock import MagicMock
from app import on_button_click

@pytest.fixture
def mock_session_state():
    st_mock = MagicMock()
    st_mock.session_state = {
        'expression': "",
        'display': "0"
    }
    return st_mock

def test_on_button_click_numeric_input(mock_session_state, monkeypatch):
    monkeypatch.setattr('streamlit.session_state', mock_session_state.session_state)
    on_button_click("5")
    assert mock_session_state.session_state.expression == "5"
    assert mock_session_state.session_state.display == "5"

def test_on_button_click_operator_input(mock_session_state, monkeypatch):
    monkeypatch.setattr('streamlit.session_state', mock_session_state.session_state)
    mock_session_state.session_state.expression = "5"
    mock_session_state.session_state.display = "5"
    on_button_click("+")
    assert mock_session_state.session_state.expression == "5+"
    assert mock_session_state.session_state.display == "5+"

def test_on_button_click_equals(mock_session_state, monkeypatch):
    monkeypatch.setattr('streamlit.session_state', mock_session_state.session_state)
    mock_session_state.session_state.expression = "5+3"
    mock_session_state.session_state.display = "5+3"
    on_button_click("=")
    assert mock_session_state.session_state.display == "8"
    assert mock_session_state.session_state.expression == "8"

def test_on_button_click_clear(mock_session_state, monkeypatch):
    monkeypatch.setattr('streamlit.session_state', mock_session_state.session_state)
    mock_session_state.session_state.expression = "123"
    mock_session_state.session_state.display = "123"
    on_button_click("C")
    assert mock_session_state.session_state.expression == ""
    assert mock_session_state.session_state.display == "0"

def test_on_button_click_backspace(mock_session_state, monkeypatch):
    monkeypatch.setattr('streamlit.session_state', mock_session_state.session_state)
    mock_session_state.session_state.expression = "123"
    mock_session_state.session_state.display = "123"
    on_button_click("DEL")
    assert mock_session_state.session_state.expression == "12"
    assert mock_session_state.session_state.display == "12"

def test_on_button_click_division_by_zero(mock_session_state, monkeypatch):
    monkeypatch.setattr('streamlit.session_state', mock_session_state.session_state)
    mock_session_state.session_state.expression = "10\u00F70"
    mock_session_state.session_state.display = "10\u00F70"
    on_button_click("=")
    assert mock_session_state.session_state.display == "Error"
    assert mock_session_state.session_state.expression == ""
