# link: https://leetcode.com/problems/string-to-integer-atoi/
def string_to_int(s):
    """
    convert string to int.

    Parameters
    ----------
    s: str
        a string that will be converted to integer

    Returns
    -------
    out: int
        the integer that is the conversion of string
    """

    lst = [str(x) for x in range(10)]
    is_positive = True

    is_space = True
    for i, elem in enumerate(s):
        if elem != " ":
            is_space = False
            break

    if is_space:
        return 0

    num_str = ""
    idx = i
    is_positive = True
    if s[idx] == "-":
        is_positive = False
    else:
        if s[idx] in lst:
            num_str += s[idx]



    for j in range(idx + 1, len(s)):
        if s[j] in lst:
            num_str += s[j]
        else:
            break

    if len(num_str) == 0:
        return 0


    max_val = 2147483647
    min_val = -2147483648
    if is_positive:
        coef = 1
        ref_str = str(abs(max_val))
    else:
        coef = -1
        ref_str = str(abs(min_val))

    if len(num_str) < 10:
        out = coef * int(num_str)
    elif len(num_str) > 10:
        out = coef * int(ref_str)
    else:
        # num-of-digits is 10. need to be checked!
        is_greater = False
        for i, digit_str in enumerate(num_str):
            if digit_str == ref_str:
                continue
            elif digit_str < ref_str:
                break
            else:
                is_greater = True
                break

        if is_greater:
            out = coef * int(ref_str)
        else:
            out = coef * int(num_str)

    return out
