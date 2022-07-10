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

    num_str = ""
    for i, elem in enumerate(s):
        if elem == " ":
            continue

        if elem == "-":
            is_positive = False

        if elem in lst:
            num_str += elem


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
