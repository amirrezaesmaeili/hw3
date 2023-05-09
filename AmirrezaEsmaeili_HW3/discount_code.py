def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount Percent and Calculate Final Price

    Args:
        price (int): The original price.
        discount (float): The discount percentage. Default is 0.0.

    Returns:
        int: The final discounted price.

    Raises:
        AssertionError: If the final price is not greater than 0 and less than the original price.
    """
    final_price = int(price * (1 - discount))
    assert 0 < final_price < price, "The final price is not within the expected range."
    return final_price


# output for 100 price and 0.02 or 20% discount is --> 80
final_price = apply_discount(100, 0.20)
print(final_price)
