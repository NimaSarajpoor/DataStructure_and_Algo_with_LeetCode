# link: https://leetcode.com/problems/longest-palindromic-substring/

def naive_longest_sub_palindrom(s):
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
    # aba --> abas
    # abccbcddddc --> cddddc

    if len(s) == 1:
        return s

    out = [0, 1] # start, stop
    max_length = 1
    for i in range(len(s)-1):
        if len(s) - i <= max_length:
            break
        for j in range(i + 1, len(s) + 1):
            if j - i <= max_length:
                continue
            if s[i:j] == s[i:j][::-1]:
                out = [i, j]
                max_length = j - i

    return s[out[0]:out[1]]


def naive_longest_sub_palindrom_enhanced(s):
    """
    This is the enhanced version of naive implementation

    Finds the longest substring with palindromic property "NIMAMIN"

    Parameters
    ----------
    s: str
        A string with digits and english letters

    Returns
    -------
    out: str
        A string that is the longest substring of `s` and it is palindrom

    Example:
    s = "Goozoo"
    >>> longest_sub_palindrom(s)
    "oozoo"
    """
    out = [0, 1] #start, stop
    prev_max_length = 1


    for i in range(len(s) - 1):
        j = 1
        while (i - j >= 0) and (i + j < len(s)):
            if s[i - j] == s[i + j]:
                j += 1
        max_length = max(prev_max_length, 2 * (j - 1) + 1)
        if max_length > prev_max_length:
            prev_max_length = max_length
            out = [i - (j - 1), i + j]

        # twin case
        if s[i] == s[i + 1]:
            j = 1
            while (i - j >= 0) and (i + 1 + j < len(s)):
                if s[i - j] == s[i + 1 + j]:
                    j += 1

            max_length = max(prev_max_length, 2 * (j - 1) + 2)
            if max_length > prev_max_length:
                prev_max_length = max_length
                out = [i - (j - 1), i + 1 + j]


    return s[out[0]:out[1]]
