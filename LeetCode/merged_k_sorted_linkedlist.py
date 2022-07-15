# link: https://leetcode.com/problems/merge-k-sorted-lists/
from core import Node

def merge_k_sorted_linkedlist(L):
    """
    merge k sorted linkedlist and return its head

    Parameters
    ----------
    L : List
        a list of objects, where each object is the head of a sorted linkedlist.
        this object comes with two attributes `val` (value contained in the node)
        and `next` (a pointer that points to the next object)

    Returns
    -------
    out : object
        the head of merged sorted linkedlist
    """
    if len(L) == 0:
        return None

    dummy = Node(0)
    current_node = dummy

    head_prev = L[0]
    for i in range(1, len(L)):
        head_new = L[i]
        while head_new is not None or head_prev is not None:
            if head_new is None:
                current_node.next = head_prev
                break

            if head_prev is None:
                current_node.next = head_new
                break

            val_a = head_prev.val
            val_b = head_new.val
            if val_a <= val_b:
                current_node.next = Node(val_a)
                head_prev = head_prev.next
            else:
                current_node.next = Node(val_b)
                head_new = head_new.next

            current_node = current_node.next

    return dummy.next
