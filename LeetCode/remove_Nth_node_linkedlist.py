# link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/


def removeNthFromEnd(head, n):
    """
    Given the head of a linkedlist, remove its nth node from the end, and return
    the head of the updated linkedlist. (e.g. with n=1, we basically remove the
    last node)

    Parameters
    ----------
    head : object
        An object with two attributes (val and next). This is head of a linked list
        The size of this linkedlist, `sz`, is at least 1.

    n : int
        An integer in range 1(inclusive) to sz(inclusive), indicates the node
        position from the end of  linkedlist

    Returns
    -------
    head: object
        The updated head after removing the  n-th node from the end of linkedlist
    """
    current_node = head
    n_node = 0
    while current_node is not None:
        current_node = current_node.next
        n_node += 1

    n_from_head = n_node - n

    node_id = 0
    current_node = head
    prev_node = None
    while current_node is not None:
        if node_id == n_from_head:
            break
        prev_node = current_node
        current_node = current_node.next
        node_id += 1

    if prev_node is None:
        head = current_node.next
    else:
        prev_node.next = current_node.next

    return head
