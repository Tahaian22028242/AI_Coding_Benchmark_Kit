
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = []
    # Iterate through all numbers except the last one
    for number in numbers[:-1]:
        # For each of these, add the number and the delimeter to the result list
        result.extend([number, delimeter])
    
    # Finally, append the last number from the original list, which doesn't get a delimeter after it.
    result.append(numbers[-1])
    
    return result