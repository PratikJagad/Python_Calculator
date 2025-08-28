def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the multiply of a and b."""
    return a * b

def Division(a, b):
    """Return the divison of a and b."""
    try:
        return a / b
    except ZeroDivisionError:
        return " Error: Division by zero is not allowed"

if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiply:", multiply(5, 3))
    print("Divison:", Division(5, 3))