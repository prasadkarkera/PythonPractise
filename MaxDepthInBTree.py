class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def max_depth_util(root, depth):

    if root is None:
        return depth

    left_depth = max_depth_util(root.left, depth + 1)
    right_depth = max_depth_util(root.right, depth + 1)

    return max(left_depth, right_depth)


head = Node(9)
head.left = Node(4)
head.right = Node(17)

head.left.left = Node(3)
head.left.right = Node(6)

head.left.right.left = Node(5)
head.left.right.left.left = Node(19)
head.left.right.right = Node(7)

head.right.right = Node(22)
head.right.right.left = Node(20)


print(max_depth_util(head, 0))
