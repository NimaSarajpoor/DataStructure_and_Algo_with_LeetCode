# link: https://leetcode.com/problems/3sum-closest/
def three_sum_closest(nums, target):
    """
    Given an integer array nums of length n and an integer target, it will find
    three integers in nums such that the sum is closest to target. It returns the
    sum of the three integers.

    Parameters
    ----------
    nums : List
        A list of interger values

    target : int
        An integet

    Returns
    -------
    out : int
        The closest possible value to target that can be sum of three elements of
        `nums`
    """
    nums.sort()

    closest_so_far = float("inf")
    out = float("inf")

    for idx, v in enumerate(nums[:-2]):
        i = idx + 1
        j = len(nums) - 1

        for _ in range(len(nums)):  # upper bound for number of iterations
            if i >= j:
                break

            s = nums[i] + nums[j] + v
            net_val = s - target
            if abs(net_val) < closest_so_far:
                closest_so_far = abs(net_val)
                out = s

            if net_val == 0:
                return out

            if net_val > 0:
                j -= 1
            else:
                i += 1

    return out
