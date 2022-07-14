from find_max_container import find_max_container
import numpy as np

def naive_find_max_container(height):
    """
    height is list of interger values
    """
    best_so_far = -1
    for  i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            v = (j - i) * min(height[i], height[j])
            best_so_far = max(best_so_far, v)

    return best_so_far


def test_find_max_container():

    for n in range(2, 20):
        height = np.random.randint(0, 100, size=n)
        ref = naive_find_max_container(height)
        comp = find_max_container(height)

        assert comp == ref
