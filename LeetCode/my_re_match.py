# hard: https://leetcode.com/problems/regular-expression-matching/


def my_re_match(s, p):
    """
    finds if the string `s` and the string `p` can be matched or not.

    Note: * means zero or more of  preceding character and . means any character
    (so, `p = ".*"` can match any string.)

    Parameters
    ----------
    s : str
        a string value

    p : str
        a string value

    Returns
    -------
    out : bool
        True if `s` and `p` can be matched.
    """
    # need to find all possible branches


    # "abcdefg"
    # "xxxxxxx"
    # "xxx.xxxx"
    # "xxx.*xxxx"
    # "xxx.xx*xx"
    # "xxx*xxxx"

    # "s"
    # "aa*aa"
