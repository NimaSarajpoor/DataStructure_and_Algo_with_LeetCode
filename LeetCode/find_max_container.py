# link: https://leetcode.com/problems/container-with-most-water/
def find_max_container(height):
    """
    find max value of abs(v), where v is (i - j) * (height[i] - height[j])

    Parameters
    ----------
    height : list
        a list of integer values in range 0 to 10^4.
        the length of list is at least 2.

    Returns
    -------
    out: int
        maximum value of abs(v)
    """
    out = -1

    i = 0  # left pointer
    j = len(height) - 1  # right pointer
    for _ in range(len(height)):
        if height[i] <= height[j]:
            v = (j - i) * height[i]
            i += 1
        else:
            v = (j - i) * height[j]
            j -= 1

        out = max(out, v)

    return out

    
