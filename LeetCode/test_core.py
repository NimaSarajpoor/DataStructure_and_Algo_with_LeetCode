import core
import numpy as np
from numpy import testing as npt

def test_Node():
    val = np.random.rand()
    node = core.Node(val)

    npt.assert_equal(node.val, val)
