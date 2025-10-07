
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    >>> has_close_elements([], 0.5)
    False
    >>> has_close_elements([5.0], 1.0)
    False
    >>> has_close_elements([1.0, 2.0, 3.9, 7.0], 1.1)
    True
    """
    # Sort the list. If any two elements are closer than the threshold,
    # then two adjacent elements in the sorted list must be.
    # This is because the smallest difference between any two elements
    # will be found between adjacent elements once the list is sorted.
    numbers.sort()

    # Iterate through the sorted list and compare each element with the next one.
    for i in range(len(numbers) - 1):
        # Since the list is sorted, numbers[i+1] will always be >= numbers[i].
        # We don't need to use abs().
        diff = numbers[i+1] - numbers[i]
        if diff < threshold:
            return True

    # If the loop completes without finding any close elements, return False.
    return False
