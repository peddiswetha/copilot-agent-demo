def validate_numeric_inputs(*values):
    validated = []
    for value in values:
        try:
            validated.append(float(value))
        except (TypeError, ValueError):
            raise TypeError("Inputs must be numeric")
    return validated


def add(a, b):
    a, b = validate_numeric_inputs(a, b)
    return a + b


def subtract(a, b):
    a, b = validate_numeric_inputs(a, b)
    return a - b


def multiply(a, b):
    a, b = validate_numeric_inputs(a, b)
    return a * b


def divide(a, b):
    a, b = validate_numeric_inputs(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    print("Add:", add(5, 3))
    print("Subtract:", subtract(10, 4))
    print("Multiply:", multiply(6, 7))
    print("Divide:", divide(20, 4))
