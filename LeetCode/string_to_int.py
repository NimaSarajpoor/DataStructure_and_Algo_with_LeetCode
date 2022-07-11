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

    lst = [str(x) for x in range(10)] # digits in str

    is_space = True
    for i, elem in enumerate(s):
        if elem != " ":
            is_space = False
            break

    if is_space:
        return 0

    # we have at least non-space character
    num_str = ""
    idx = i
    is_positive = True
    if s[idx] == "-":
        is_positive = False
        start_idx = idx + 1
    elif s[idx] == "+":
        start_idx = idx + 1
    else:
        start_idx = idx

    for j in range(start_idx, len(s)):
        if s[j] in lst:
            num_str += s[j]
        else:
            break

    # remove leading zeros
    for i, x in enumerate(num_str):
        if x != "0":
            break
    num_str = num_str[i:]
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
            if digit_str == ref_str[i]:
                continue
            elif digit_str < ref_str[i]:
                break
            else:
                is_greater = True
                break

        if is_greater:
            out = coef * int(ref_str)
        else:
            out = coef * int(num_str)

    return out


# cleaner code:
# https://leetcode.com/problems/string-to-integer-atoi/discuss/647916/Python%3A-String-parsing-with-regex

# note that we prefer to figure out if the string exceeds the range or not. It
# is not reasonable to convert string to integer and then limit it to min/max
# bounds.

# learn how to use regex to parse strings.
# Also see: https://www.youtube.com/watch?v=K8L6KVGG-7o
