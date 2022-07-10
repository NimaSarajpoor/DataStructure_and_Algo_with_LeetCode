# link: https://leetcode.com/problems/reverse-integer/submissions/

def reverse_int(x):
    """
    reverse x. If it is outside of a signed 32-bit integer range, then
    return 0

    Parameters
    ----------
    x: int
        a signed 32-bit integer range

    Returns
    -------
    out: int
        reverse of x. If the output is outside of signed 32-bit range,
        then return 0
    """
    out = None

    if x == 0:
        return x

    max_val = 2147483647
    min_val = -2147483648

    if x < 0:
        coef = -1
        ref = str(abs(min_val))
    else:
        coef = 1
        ref = str(abs(max_val))

    x_str = str(abs(x))
    x_str_reversed = x_str[::-1]
    if len(x_str_reversed) > 10:
        out =  0
    elif len(x_str_reversed) < 10:
        out = coef * int(x_str_reversed)
    else:
        # len(x_str_reversed) is exactly 10.
        for i, s in enumerate(x_str_reversed):
            if int(s) == int(ref[i]):
                continue
            elif int(s) < int(ref[i]):
                out = coef * int(x_str_reversed)
                break
            else:
                out = 0
                break

        if out is None:
            out = coef * int(x_str_reversed)

    return out
