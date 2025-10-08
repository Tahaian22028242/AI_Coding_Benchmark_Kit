# Prompt:
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """


# Model: google_gemini

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # A brute-force approach would be to use nested loops to compare every pair
    # of numbers, which would be O(n^2).
    # A more efficient approach is to first sort the list. If any two elements
    # in the original list are close, then two *adjacent* elements in the sorted
    # list must also be close. This reduces the complexity from O(n^2) to
    # O(n log n) due to the sort.

    # Edge case: If there are 0 or 1 elements, no pair exists.
    if len(numbers) < 2:
        return False

    # Sort the list in ascending order.
    sorted_numbers = sorted(numbers)

    # Iterate through the sorted list and check the difference between adjacent elements.
    for i in range(len(sorted_numbers) - 1):
        # Since the list is sorted, sorted_numbers[i+1] >= sorted_numbers[i],
        # so we don't need to take the absolute value of the difference.
        difference = sorted_numbers[i+1] - sorted_numbers[i]
        
        if difference < threshold:
            return True

    # If the loop completes without finding any pair closer than the threshold.
    return False

```
