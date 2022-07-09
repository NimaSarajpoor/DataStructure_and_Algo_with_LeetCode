# link: https://leetcode.com/problems/longest-palindromic-substring/

def longest_sub_palindrom(s):
    """
    finds the longest substring with palindromic property "NIMAMIN"

    Parameters
    ----------
    s: str
        a string with digits and english letters

    Returns
    -------
    out: str
        a string that is the longest substring of `s` and it is palindrom

    Example:
    s = "Goozoo"
    >>> longest_sub_palindrom(s)
    "oozoo"
    """
    # Example:
    # a --> a
    # ab --> a , b
    # abb --> bb
    # aab --> aa
    # aaa --> aaa
    # aba --> aba
    # abccbcddddc --> cddddc

    if len(s) == 1:
        return s

    out = s[0]
    max_length = 1
    for i in range(len(s)-1):
        for j in range(i + 1, len(s)):
            if i - j <= max_length:
                continue
            if s[i:j] == s[i:j][::-1]:
                out = s[i:j]
                max_length = len(out)

    return out
