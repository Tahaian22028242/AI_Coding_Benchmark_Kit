
    if not string:
        return ""

    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            # The first palindromic suffix found when iterating from the start
            # of the string corresponds to the longest one.
            # The prefix is the part of the string that comes before this suffix.
            prefix = string[:i]
            
            # To make the entire string a palindrome, we append the reverse of
            # the prefix to the original string.
            return string + prefix[::-1]
    
    # This line is theoretically unreachable for non-empty strings, as a single
    # character suffix is always a palindrome. It's included for completeness,
    # though the loop above will always return a value.
    return string
