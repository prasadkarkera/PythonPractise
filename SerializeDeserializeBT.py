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


# Global variable to keep iterating through the queue
i = -1
def deserialize(root, queue):
    global i
    i = i + 1
    if i > len(queue) or queue[i] == -1:
        return
    root.value = queue[i]
    # We need to create new nodes for the children otherwise you will be passing None in recursion
    root.left = Node(-1)
    root.right = Node(-1)
    
    deserialize(root.left, queue)
    deserialize(root.right, queue)
    
    # We need to remove nodes that don't have value.
    if root.left.value == -1:
        root.left = None
    if root.right.value == -1:
        root.right = None
    return root

head = Node(26)
head.left = Node(11)
head.right = Node(3)

head.left.left = Node(3)
head.left.right = Node(6)

head.right.right = Node(3)
print(serialize(head, []))

new_head = Node(0)

print(serialize(deserialize(new_head, serialize(head, [])), []))
