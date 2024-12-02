class Calculator:
    """A simple calculator class with basic and advanced operations."""

    @staticmethod
    def add(a, b):
        Calculator._validate_input(a, b)
        return a + b

    @staticmethod
    def subtract(a, b):
        Calculator._validate_input(a, b)
        return a - b

    @staticmethod
    def multiply(a, b):
        Calculator._validate_input(a, b)
        return a * b

    @staticmethod
    def divide(a, b):
        Calculator._validate_input(a, b)
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    @staticmethod
    def power(base, exponent):
        """Calculate base raised to the power of exponent."""
        Calculator._validate_input(base, exponent)
        return base ** exponent

    @staticmethod
    def square_root(a):
        """Calculate the square root of a number."""
        if not isinstance(a, (int, float)):
            raise TypeError("Input must be a number.")
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return a ** 0.5

    @staticmethod
    def modulo(a, b):
        """Calculate the remainder of a division."""
        Calculator._validate_input(a, b)
        if b == 0:
            raise ValueError("Modulo by zero is not allowed.")
        return a % b

    @staticmethod
    def factorial(a):
        """Calculate the factorial of a number."""
        if not isinstance(a, int):
            raise TypeError("Input must be an integer.")
        if a < 0:
            raise ValueError("Factorial of a negative number is not defined.")
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    @staticmethod
    def _validate_input(a, b):
        """Helper method to validate input types."""
        if not all(isinstance(i, (int, float)) for i in (a, b)):
            raise TypeError("Inputs must be numbers.")
