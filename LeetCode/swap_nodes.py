# link: https://leetcode.com/problems/swap-nodes-in-pairs/
def swap_nodes(head):
    """
    Given the head of linkedlist, swap adjacent nodes starting from head, and
    return the head of the new linkedlist

    head : a node object with attributes `next` and `val`
    """
    if head is None or head.next is None:
        return head

    curr_node = head
    prev_node = None
    while curr_node is not None and curr_node.next is not None:
        next_node = curr_node.next
        tmp = next_node.next
        if prev_node is None:
            head = next_node
        else:
            prev_node.next = next_node
        next_node.next = curr_node
        curr_node.next = tmp
        prev_node = curr_node
        curr_node = tmp

    return head
