# https://leetcode.com/problems/merge-two-sorted-lists/
from core import Node


def mergeTwoLists(list1, list2):
    """
    Given the head of two sorted linkedlist, merge them and return the head of
    the merged sorted linkedlist.

    Parameters
    ----------
    list1: object
        The head of the first sorted linkedlist, with two attributes `val` and `next`

    list2: object
        The head of the second sorted linkedlist, with two attributes `val` and `next`

    Returns
    -------
    out : object
        The head of the merged sorted linkedlist
    """
    dummy = Node(0)
    current_node = dummy
    while list1 is not None or list2 is not None:
        if list1 is None:
            current_node.next = list2
            break
        elif list2 is None:
            current_node.next = list1
            break
        else:
            val1 = list1.val
            val2 = list2.val
            if val1 <= val2:
                current_node.next = Node(val1)
                list1 = list1.next
            else:
                current_node.next = Node(val2)
                list2 = list2.next

            current_node = current_node.next

    return dummy.next
