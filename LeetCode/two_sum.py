# link: https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    """
    this function gets a list of integers `nums` and return indices of two
    elementst that they add up to `target`

    assumption: each input has exactly one solution, and there is no repeated value
    constraints: please see https://leetcode.com/problems/two-sum/

    Parameters
    ----------
    nums: list
        list of integers, with minimum length of two.

    target: int
        the number that is the summation of two elements from `nums`

    Returns
    -------
    out: list
        a list of length two that contains the indices of elements from `nums`
        whose sum is `target`
    """

    positions = {}
    print('nums: ', nums)
    for i, val in enumerate(nums):
        if target - val in positions.keys():
            return [positions[target - val], i]

        positions[val] = i

    return [-1, -1]
