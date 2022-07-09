import core
from core import Node, LinkedList
import numpy as np
from numpy import testing as npt

def test_Node():
    val = np.random.rand()
    node = core.Node(val)

    npt.assert_equal(node.val, val)
    assert node.next is None


def test_LinkedList_root():
    L = LinkedList()
    assert L.root is None

    val = np.random.rand()
    L.insert_val(val)

    npt.assert_equal(L.root.val, val)
    assert L.root.next is None


def test_LinkedList_list():
    arr = np.random.rand(5)
    L = LinkedList()
    L.insert_from_list(arr)
    npt.assert_almost_equal(arr[::-1], np.array(L.convert_to_lst()))
