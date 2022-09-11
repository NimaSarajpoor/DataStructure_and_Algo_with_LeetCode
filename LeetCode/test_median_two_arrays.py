from median_two_arrays import get_median_two_sorted_arrays


def test_OneListEmpty():
    nums1 = []
    nums2 = [10, 20, 30]

    ref = 20
    assert get_median_two_sorted_arrays(nums1, nums2) == ref
    assert get_median_two_sorted_arrays(nums2, nums1) == ref


def test_SingleElement():
    nums1 = [5]
    nums2 = []

    ref = 5
    assert get_median_two_sorted_arrays(nums1, nums2) == ref
    assert get_median_two_sorted_arrays(nums2, nums1) == ref


def test_BothEven():
    nums1 = [4, 7, 8, 10]
    nums2 = [1, 3, 5, 6]

    ref = 5.5
    assert get_median_two_sorted_arrays(nums1, nums2) == ref
    assert get_median_two_sorted_arrays(nums2, nums1) == ref


def test_BothOdd():
    nums1 = [4, 7, 8]
    nums2 = [1, 3, 5]

    ref = 4.5
    assert get_median_two_sorted_arrays(nums1, nums2) == ref
    assert get_median_two_sorted_arrays(nums2, nums1) == ref


def test_EvenOdd():
    nums1 = [7, 9]
    nums2 = [1, 3, 8]

    ref = 7
    assert get_median_two_sorted_arrays(nums1, nums2) == ref
    assert get_median_two_sorted_arrays(nums2, nums1) == ref


def test_OneListAllSmall():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7, 8, 9, 10]

    ref = 5.5
    assert get_median_two_sorted_arrays(nums1, nums2) == ref
    assert get_median_two_sorted_arrays(nums2, nums1) == ref
