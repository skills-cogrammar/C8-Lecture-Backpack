# advanced_operations.py

def power(x: float, y: float) -> float:
    """
    Raises x to the power of y.
    
    Args:
        x (float): The base number.
        y (float): The exponent.
    
    Returns:
        float: The result of x raised to the power of y.
    """
    return x ** y


def square_root(x: float) -> float:
    """
    Returns the square root of x.
    
    Args:
        x (float): The number to find the square root of.
    
    Returns:
        float: The square root of x.
    """
    return x ** 0.5


def absolute_value(x: float) -> float:
    """
    Returns the absolute value of x.
    
    Args:
        x (float): The number to find the absolute value of.
    
    Returns:
        float: The absolute value of x.
    """
    return abs(x)


def factorial(x: int) -> int:
    """
    Returns the factorial of x.
    
    Args:
        x (int): A non-negative integer.
    
    Returns:
        int: The factorial of x.
    """
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
