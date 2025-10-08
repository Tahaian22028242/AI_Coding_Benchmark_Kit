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
    >>> find_closest_elements([5.0, -1.0, 10.0, 3.0])
    (3.0, 5.0)
    """
    # Sort the list of numbers. The two closest elements will be adjacent in the sorted list.
    sorted_numbers = sorted(numbers)

    # Initialize variables to track the minimum difference and the corresponding pair.
    # We can start with the difference between the first two elements.
    min_difference = float('inf')
    closest_pair = (0.0, 0.0)

    # Iterate through the sorted list and compare adjacent elements.
    for i in range(len(sorted_numbers) - 1):
        num1 = sorted_numbers[i]
        num2 = sorted_numbers[i+1]
        difference = num2 - num1

        # If we find a smaller difference, update our tracking variables.
        if difference < min_difference:
            min_difference = difference
            closest_pair = (num1, num2)

    return closest_pair
```
