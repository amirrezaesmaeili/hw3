import math


def divide_numbers(a: float, b: float) -> float:
    """
    Divide two numbers and return the result.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of dividing a by b.

    LBYL Approach:
    - Look before you leap: Check conditions before performing the division.
    - If the denominator is zero, return math.inf (positive infinity) and
      print a message explaining the meaning of INF.
    - If either a or b is not of type int or float, raise a ValueError.
    - Otherwise, perform the division and return the result.
    """
    if b == 0:
        print("INF represents positive infinity")
        result = math.inf
    elif not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Invalid input. Both a and b must be numeric.")
    else:
        result = a / b
    return result
