
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
    # Iterate through all elements except the last one
    for number in numbers[:-1]:
        result.append(number)
        result.append(delimeter)
    
    # Add the last element without a delimeter after it
    result.append(numbers[-1])
    
    return result