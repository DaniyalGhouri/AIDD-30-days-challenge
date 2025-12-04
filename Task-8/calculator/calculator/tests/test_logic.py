import pytest
from calculator.calculator_logic import add_value, evaluate_expression, clear_expression, backspace_delete

def test_add_value_numeric_input():
    assert add_value("", "5") == "5"
    assert add_value("5", "3") == "53"
    assert add_value("123", "+") == "123+"

def test_evaluate_expression_basic_arithmetic():
    assert evaluate_expression("5+3") == "8"
    assert evaluate_expression("10-4") == "6"
    assert evaluate_expression("2*6") == "12"
    assert evaluate_expression("15/3") == "5"
    assert evaluate_expression("5+3*2") == "11" # Operator precedence
    assert evaluate_expression(" (5+3)*2") == "16"

def test_evaluate_expression_division_by_zero():
    assert evaluate_expression("10/0") == "Error"

def test_evaluate_expression_invalid_input():
    assert evaluate_expression("5+") == "Error"
    assert evaluate_expression("abc") == "Error"
    assert evaluate_expression("5++3") == "Error"

def test_add_value_decimal_input():
    assert add_value("", ".") == "."
    assert add_value("5", ".") == "5."
    assert add_value("5.", "3") == "5.3"
    assert add_value("0", ".") == "0."
    assert add_value("0.", "5") == "0.5"

def test_evaluate_expression_decimal_arithmetic():
    assert evaluate_expression("2.5+1.5") == "4.0"
    assert evaluate_expression("7.5*2") == "15.0"
    assert evaluate_expression("10.5-3.2") == "7.3"
    assert evaluate_expression("9.9/3") == "3.3"
    assert evaluate_expression("1.1+2.2+3.3") == "6.6"

def test_clear_expression():
    expression, display = clear_expression()
    assert expression == ""
    assert display == "0"

def test_backspace_delete():
    # Test deleting a digit
    expression, display = backspace_delete("123", "123")
    assert expression == "12"
    assert display == "12"

    # Test deleting an operator
    expression, display = backspace_delete("12+", "12+")
    assert expression == "12"
    assert display == "12" # Display should revert to previous number or clear

    # Test deleting to empty
    expression, display = backspace_delete("1", "1")
    assert expression == ""
    assert display == "0"

    # Test deleting from empty
    expression, display = backspace_delete("", "0")
    assert expression == ""
    assert display == "0"
