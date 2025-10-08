# Prompt:


def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """


# Model: google_gemini

```python
    if not string:
        return ''

    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            # Found the longest palindromic suffix. It's `string[i:]`.
            # The part that needs to be mirrored is the prefix before this suffix.
            prefix = string[:i]
            # Append the reverse of the prefix to the original string.
            return string + prefix[::-1]
    
    # This line is technically unreachable for any non-empty string,
    # as the last character of any string is a palindrome by itself.
    # The loop will always find a match at i = len(string) - 1 at the latest.
    # It is included for logical completeness in case of unexpected behavior.
    return string
```
