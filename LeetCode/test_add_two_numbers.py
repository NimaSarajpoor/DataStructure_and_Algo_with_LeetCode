from core import Node, Linkedlist
from add_two_numbers import add_two_numbers



def test_add_linkedlist():
    lst_A = [1, 2, 3]
    A = Linkedlist()
    A.insert_from_list(lst_A)

    lst_B = [0]
    B = Linkedlist()
    B.insert_from_list(lst_B)

    A_plus_B = Linkedlist()
    A_plus_B.root = add_two_numbers(A.root, B.root)
    comp = A_plus_B.convert_to_lst()

    ref = int("".join([str(x) for x in lst_A])) + int("".join([str(x) for x in lst_B]))

    assert ref == int("".join([str(x) for x in comp[::-1]]))
