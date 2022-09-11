from two_sum import two_sum
import numpy as np


def test_two_sum():
    a = np.random.randint(150, high=1000)
    for m in range(2, 100):
        nums = np.random.choice(a, size=m, replace=False)

        IDX = np.random.choice(np.arange(m), size=2, replace=False)
        target = np.random.randint(10000, high=20000)
        nums[IDX[1]] = target - nums[IDX[0]]

        comp = two_sum(nums, target)

        ref = np.sort(IDX).tolist()
        comp = sorted(comp)

        assert ref == comp
