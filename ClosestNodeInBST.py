# http://www.geeksforgeeks.org/find-closest-element-binary-search-tree/
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def closest_node_util(root, number_to_search, min_diff, min_value):

    if root is None:
        return min_diff, min_value

    if number_to_search == root.value:
        return 0, root.value

    new_diff = abs(root.value - number_to_search)

    if min_diff > new_diff:
        min_diff = new_diff
        min_value = root.value

    if root.value < number_to_search:
        min_diff, min_value = closest_node_util(root.right, number_to_search, min_diff, min_value)
    else:
        min_diff, min_value = closest_node_util(root.left, number_to_search, min_diff, min_value)

    return min_diff, min_value


def closest_node_in_bst(root, num_to_search):
    min_diff, min_value = closest_node_util(root, num_to_search, sys.maxsize, None)
    return min_value


head = Node(9)
head.left = Node(4)
head.right = Node(17)

head.left.left = Node(3)
head.left.right = Node(6)

head.left.right.left = Node(5)
head.left.right.right = Node(7)

head.right.right = Node(22)
head.right.right.left = Node(20)

print(closest_node_in_bst(head, 17))
