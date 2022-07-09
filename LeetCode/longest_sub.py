# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def len_longest_substr(s):
    """
    find the length of the longst substring without repeating characters

    Parameters
    ----------
    s: str
        a string that consists of English letters, digits, symbols, and spaces

    Returns
    -------
    out: str
        the longest substring of s without repearing characters


    Examples:
    >>> find_longest_substr("abcabcbb")
    3
    because, the longest substring is "abc" whose length is 3.
    """
    best_so_far = 0
    sub_hash = {}
    for i in range(len(s)):
        if s[i] not in sub_hash.keys():
            sub_hash[s[i]] = i
            best_so_far = max(best_so_far, len(sub_hash.keys()))
        else:
            for key in sub_hash.keys():
                if key == s[i]:
                    del sub_hash[key]
                    break
                del sub_hash[key]

            sub_hash[s[i]] = i

        return best_so_far
