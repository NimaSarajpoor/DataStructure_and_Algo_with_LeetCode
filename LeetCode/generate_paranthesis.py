# link: https://leetcode.com/problems/generate-parentheses/


def generate_parenthesis(n):
    """
    for `n` pair of paranthesis, returns all possible valid
    combinations.

    Examples:
    generate_parenthesis(2)
    >>> (()), ()()

    Parameters
    ----------
    n : int
        An integer in range 1(inclusive) to 8(inclusive)

    Returns
    -------
    out : List
        a list of strings, where each string is one unique combination of paranthesis
        that is valid.
    """
    # () --> 01
    # (()) ()() --> 0011 0101
    # 000111 001011 001101 010011 010101

    # 010011, 001011, 000111, 010101, 001101

    # insert pack `01` but not after the first 1 (Trick!)

    out = ["()"]
    for _ in range(1, n):
        tmp = []
        for item in out:
            for i, c in enumerate(item):
                if c == ")":
                    break
                tmp.append(item[:i] + "()" + item[i:])
            tmp.append(item[:i] + "()" + item[i:])

        out = [x for x in tmp]

    return out
