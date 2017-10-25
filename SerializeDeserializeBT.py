class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def serialize(root, queue):
    if root is None:
        queue.append(-1)
        return

    queue.append(root.value)
    serialize(root.left, queue)
    serialize(root.right, queue)
    return queue


def deserialize(root, queue, i):
    if i > len(queue) or queue[i] == -1 or root is None:
        return

    root.value = queue[i]
    deserialize(root.left, queue, i + 1)
    deserialize(root.right, queue, i + 1)
    return head

head = Node(26)
head.left = Node(11)
head.right = Node(3)

head.left.left = Node(3)
head.left.right = Node(6)

head.right.right = Node(3)
print(serialize(head, []))

new_head = Node(0)

print(deserialize(new_head, serialize(head, []), 0))