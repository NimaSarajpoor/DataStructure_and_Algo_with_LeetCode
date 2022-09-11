from merge_two_sorted_linkedlist import mergeTwoLists

def merge_linkedlists(lists):
    head = None
    for i in range(len(lists)):
        new_head = lists[i]
        if new_head is None:
            continue

        head = mergeTwoLists(head, new_head)

    return head
