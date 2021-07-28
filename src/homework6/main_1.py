def avg(numbers):
    """Calculate average"""
    total = 0
    for item in numbers:
        total += item
    return total / len(numbers)