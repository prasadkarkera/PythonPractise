# http://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree/


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_tree(root, is_sum_tree):

    if not is_sum_tree:  # important condition
        return False, 0

    if root is None:
        return True, 0

    if root.left is None and root.right is None:
        return True, root.value

    is_sum_tree, left_sum = sum_tree(root.left, is_sum_tree)
    is_sum_tree, right_sum = sum_tree(root.right, is_sum_tree)

    if (left_sum + right_sum) == root.value:
        return True, left_sum + right_sum + root.value
    else:
        return False, left_sum + right_sum + root.value


head = Node(26)
head.left = Node(11)
head.right = Node(3)

head.left.left = Node(3)
head.left.right = Node(6)

head.right.right = Node(3)

result, total = sum_tree(head, True)
assert result is False

head = Node(26)
head.left = Node(10)
head.right = Node(3)

head.left.left = Node(4)
head.left.right = Node(6)

head.right.right = Node(3)

result, total = sum_tree(head, True)
assert result is True
