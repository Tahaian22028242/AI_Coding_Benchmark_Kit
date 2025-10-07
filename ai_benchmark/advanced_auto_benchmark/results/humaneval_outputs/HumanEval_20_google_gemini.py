# Prompt:
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """


# Model: google_gemini

```python
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    >>> find_closest_elements([5.0, 1.0, 3.0, 4.0])
    (3.0, 4.0)
    >>> find_closest_elements([-1.0, -5.0, 2.0, -2.5])
    (-2.5, -1.0)
    """
    # Sort the list of numbers. The closest pair of numbers will always be
    # adjacent to each other in the sorted list.
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the result pair
    # with the first two elements.
    min_difference = sorted_numbers[1] - sorted_numbers[0]
    closest_pair = (sorted_numbers[0], sorted_numbers[1])

    # Iterate through the rest of the sorted list, starting from the third element.
    # We compare each element with the one that comes before it.
    for i in range(2, len(sorted_numbers)):
        current_difference = sorted_numbers[i] - sorted_numbers[i - 1]
        
        # If we find a new smaller difference, update our result.
        if current_difference < min_difference:
            min_difference = current_difference
            closest_pair = (sorted_numbers[i - 1], sorted_numbers[i])

    # The pair is already ordered because we are working with a sorted list.
    return closest_pair

```
