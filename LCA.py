class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_lca_binary_search(node, a, b):

    if node is None:
        return

    if a < node.value and b < node.value:
        return find_lca_binary_search(node.left, a, b)

    if a > node.value and b > node.value:
        return find_lca_binary_search(node.right, a, b)

    return node


def find_lca_binary_tree_util(node, a, b, is_a_found, is_b_found):

    if node is None or (is_a_found and is_b_found):
        return None, is_a_found, is_b_found

    if node.value == a:
        is_a_found = True
        return node, is_a_found, is_b_found

    if node.value == b:
        is_b_found = True
        return node, is_a_found, is_b_found

    left_node, is_a_found, is_b_found = find_lca_binary_tree_util(node.left, a, b, is_a_found, is_b_found)
    right_node, is_a_found, is_b_found = find_lca_binary_tree_util(node.right, a, b, is_a_found, is_b_found)

    if left_node and right_node:
        return node, is_a_found, is_b_found

    if left_node is None:
        return right_node, is_a_found, is_b_found
    else:
        return left_node, is_a_found, is_b_found


def find(node, a):

    if node is None:
        return False

    if node.value == a or find(node.left, a) or find(node.right, a):
        return True

    return False


def find_lca_binary_tree(node, a, b):

    is_a_found = False
    is_b_found = False

    lca, is_a_found, is_b_found = find_lca_binary_tree_util(node, a, b, is_a_found, is_b_found)

    if (is_a_found and is_b_found) or (is_a_found and find(lca, b)) or (is_b_found and find(lca, a)):
        return lca


def main():
    tree_head = Node(1)
    tree_head.left = Node(2)
    tree_head.right = Node(3)
    tree_head.left.left = Node(4)
    tree_head.left.right = Node(5)
    tree_head.left.left.left = Node(8)
    tree_head.left.right.left = Node(9)

    tree_head.right.left = Node(6)
    tree_head.right.right = Node(7)
    tree_head.right.left.right = Node(10)
    tree_head.right.right.right = Node(11)

    lca = find_lca_binary_tree(tree_head, 5, 9)

    if lca:
        print(f'LCA = {lca.value}')
    else:
        print(f'LCA = NOT FOUND')

    tree_head = Node(20)
    tree_head.left = Node(10)
    tree_head.right = Node(30)
    tree_head.left.left = Node(5)
    tree_head.left.right = Node(15)
    tree_head.left.left.left = Node(2)
    tree_head.left.right.left = Node(11)

    tree_head.right.left = Node(21)
    tree_head.right.right = Node(32)
    tree_head.right.left.right = Node(25)
    tree_head.right.right.right = Node(33)

    lca = find_lca_binary_search(tree_head, 21, 32)

    if lca:
        print(f'LCA = {lca.value}')
    else:
        print(f'LCA = NOT FOUND')


if __name__ == '__main__':
    main()
