"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    sum = num1 + num2
    return sum


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    difference = num1 - num2
    return difference

def multiply(num1, num2):
    """Multiply the two inputs together."""

    product = num1 * num2
    return product 

def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    quotient = num1 / num2
    return quotient

def square(num1):
    """Return the square of the input."""

    sq = num1 * num1
    return sq

def cube(num1):
    """Return the cube of the input."""

    cub = num1 * num1 * num1
    return cub

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    pow = num1 ** num2
    return pow 

def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    modulus = num1 % num2
    return modulus 

def add_mult(num1, num2, num3):
    output =(num1 + num2) * num3
    return output 
    