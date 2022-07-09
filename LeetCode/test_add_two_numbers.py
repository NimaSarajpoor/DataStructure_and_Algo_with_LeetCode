from core import Node, LinkedList
from add_two_numbers import add_two_numbers



def test_add_linkedlist_edgecase():
    lst_A = [1, 2, 3]
    A = LinkedList()
    A.insert_from_list(lst_A)

    lst_B = [0]
    B = LinkedList()
    B.insert_from_list(lst_B)

    A_plus_B = LinkedList()
    A_plus_B.root = add_two_numbers(A.root, B.root)
    comp = A_plus_B.convert_to_lst()

    ref = int("".join([str(x) for x in lst_A])) + int("".join([str(x) for x in lst_B]))

    assert ref == int("".join([str(x) for x in comp[::-1]]))



def test_add_linkedlist():
    lst_A = [1, 2, 3, 4, 5]
    A = LinkedList()
    A.insert_from_list(lst_A)

    lst_B = [9, 7, 6]
    B = LinkedList()
    B.insert_from_list(lst_B)

    A_plus_B = LinkedList()
    A_plus_B.root = add_two_numbers(A.root, B.root)
    comp = A_plus_B.convert_to_lst()

    ref = int("".join([str(x) for x in lst_A])) + int("".join([str(x) for x in lst_B]))

    assert ref == int("".join([str(x) for x in comp[::-1]]))
