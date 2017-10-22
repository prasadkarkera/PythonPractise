# http://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def get_hash_map(root, hash, line_number):

    if root is None:
        return

    if hash.get(line_number):
        hash[line_number].append(root.value)
    else:
        hash[line_number] = [root.value]

    get_hash_map(root.left, hash, line_number - 1)
    get_hash_map(root.right, hash, line_number + 1)


def print_tree_vertical_order(root):

    hash_map = {}
    get_hash_map(root, hash_map, 0)

    for key, value in sorted(hash_map.items()):
        print(value)


head = Node(26)
head.left = Node(11)
head.right = Node(3)

head.left.left = Node(3)
head.left.right = Node(6)

head.right.right = Node(3)

print_tree_vertical_order(head)