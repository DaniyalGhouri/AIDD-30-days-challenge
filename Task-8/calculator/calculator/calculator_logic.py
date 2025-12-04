import math
import re # Added for regex

def add_value(current_expression, value):
    if current_expression == "0" and value.isdigit():
        return value
    return current_expression + value


def evaluate_expression(expression):
    try:
        # VALID operator patterns (allow - for negative numbers)
        # Disallow: ++, +×, ×÷, ---, etc.
        invalid = re.search(r'([+\u00D7\u00F7*/]{2,})', expression)
        if invalid:
            # allowed cases: "-4", "3*-2", "5/-3"
            if not re.search(r'[*\/\u00D7\u00F7][\-]\d', expression) and not re.match(r'^-\d', expression):
                return "Error"

        # Convert calculator symbols to Python
        expr = expression.replace('\u00D7', '*').replace('\u00F7', '/')

        # Prevent malicious patterns
        if any(bad in expr for bad in ["import", "os", "sys", "subprocess", "__"]):
            return "Error"

        # Evaluate
        result = eval(expr)

        # Format result cleanly
        if isinstance(result, float):
            if result.is_integer():
                return str(int(result))
            return f"{result:.10g}"

        return str(result)

    except:
        return "Error"


def clear_expression():
    return "", "0"

def backspace_delete(current_expression, current_display):
    if current_expression == "":
        return "", "0"
    new_expression = current_expression[:-1]
    if new_expression == "":
        return "", "0"
    return new_expression, new_expression if new_expression[-1].isdigit() else current_display
