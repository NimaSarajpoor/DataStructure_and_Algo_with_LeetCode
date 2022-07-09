# link: https://leetcode.com/problems/add-two-numbers/
from core import Node, LinkedList

def add_two_numbers(root_A, root_B):
    """
    add two linkedlist as traverse them from root and store
    the result in linkedlist

    Parameters
    ----------
    root_A: root of linkdlist A. `root_A` is an object with attribute val and next
    root_B: root of linkdlist B. `root_B` is an object with attribute val and next

    Returns
    -------
    out: root of a linkedlist that is sum of linkedlist A and B

    Example:
    linkedlist A: 1 --> 2 --> 4 --> None
    linkedlist B: 3 --> 1 --> 5 --> None

    linkedlist A + linkedlist B: 421 + 513 = 934

    So, output is: 4 --> 3 --> 9 --> None

    """
    dummy = LinkedList() # tip: we start with dummy, and we return dummy.next
    # as the root!
    dummy.root = Node(0)
    current_node = dummy.root

    c = 0
    while root_A or root_B or c:
        val = 0
        if root_A is not None:
            val += root_A.val
            root_A = root_A.next

        if root_B is not None:
            val += root_B.val
            root_B = root_B.next

        val += c

        c = val // 10
        val = val % 10

        current_node.next = Node(val)
        current_node = current_node.next

    return dummy.root.next
