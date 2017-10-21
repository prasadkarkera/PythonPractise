# http://www.geeksforgeeks.org/convert-a-given-tree-to-sum-tree/


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_sum_tree(root):

    if root is None:
        return 0

    old_value = root.value
    root.value = build_sum_tree(root.left) + build_sum_tree(root.right)

    return root.value + old_value


head = Node(26)
head.left = Node(11)
head.right = Node(3)

head.left.left = Node(3)
head.left.right = Node(6)

head.right.right = Node(3)

result = build_sum_tree(head)