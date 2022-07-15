# link: https://leetcode.com/problems/valid-parentheses/

def is_valid_paranthesis(s):
    """
    for a string `s` consisting of characters "(, ), [, ], {, }", return a boolean
    value that indicates whether this `s` is a valid paranthsis or not.

    Example:
    is_valid_paranthesis("[]")
    >>> True

    is_valid_paranthesis("}{{")
    >>> False

    Parameters
    ----------
    s : str
        a string consisting of "(, ), [, ], {, }"

    Returns
    -------
    out : bool
        True if `s` is a valid paranthesis. False otherwise.
    """
    lst = [] # stack
    mapper = {
        ')':'(',
        '}':'{',
        ']':'[',
    }

    if len(s) % 2 == 1:
        return False

    for char in s:
        if char in mapper.keys():
            char_pair = mapper[char]
            if len(lst) > 0 and lst[-1] == char_pair:
                lst.pop()
            else:
                lst.append(char)
        else:
            lst.append(char)

    if len(lst) == 0:
        return True
    else:
        return False
