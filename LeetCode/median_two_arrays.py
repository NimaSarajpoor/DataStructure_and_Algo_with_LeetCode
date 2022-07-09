import math
def get_median_two_sorted_arrays(nums1, nums2):
    """
    find the median of two sorted arrays nums1 and nums2 after being merged into
    one array

    Parameters
    ----------
    nums1: List
        a list of integer numbers sorted  in ascending order

    nums2: List
        a list of integer numbers sorted  in ascending order

    Returns
    -------
    out: int
        the median of the merge of `nums1` and `nums2`


    Examples:
    nums1 = [1, 3, 10]
    nums2 = [4, 8]
    >>> get_median_two_sorted_arrays(nums1, nums2)
    4
    """
    dummy_lst = [float('-inf'), float('inf')]
    if len(nums1) == 0:
        nums1 = dummy_lst
    if len(nums2) == 0:
        nums2 = dummy_lst


    n = len(nums1) + len(nums2)
    n_itr = math.floor(n / 2 + 1)
    # 1 2 3
    # -np.inf, np.inf
    i = 0
    j = 0
    current = float('-inf')
    for _ in range(n_itr):
        if nums1[i] <= nums2[j]:
            prev = current
            current = nums1[i]
            i = i + 1
        else:
            prev = current
            current = nums2[j]
            j = j + 1

    if n % 2 == 0: # Even
        median = (prev + current) / 2
    else:
        median = current

    return median
