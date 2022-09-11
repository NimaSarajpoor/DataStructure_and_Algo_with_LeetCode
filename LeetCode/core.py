class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# linkedlist
class LinkedList:
    def __init__(self):
        self.root = None

    def insert_val(self, val):
        new_node = Node(val)
        new_node.next = self.root
        self.root = new_node

    def remove_root(self):
        if self.root is None:
            raise ValueError("object is empty!")
        self.root = self.root.next

    def insert_from_list(self, lst):
        """
        insert values of list  from left to right. So, the last value becomes
        the root!
        """
        for val in lst:
            self.insert_val(val)

    def convert_to_lst(self):
        """
        start from root, and as we traverse, we append it to a list
        """
        return self._convert_to_lst(self.root)

    def _convert_to_lst(self, node):
        lst = []
        while node is not None:
            lst.append(node.val)
            node = node.next

        return lst
