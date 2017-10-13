# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
#
def reverse_linked_list(head, last):
    next_node = None
    prev = None
    current = head
    while current != last:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    if prev:
        print('new_head.value : {}'.format(prev.value))
    return prev


def reverseNodesInKGroups(l, k):
    current = l
    last = l
    prev_head = None
    prev_tail = None
    while last:
        for i in range(k):
            if last:
                last = last.next
            else:
                prev_tail.next = current
                return l

        # print(last.value)
        new_head = reverse_linked_list(current, last)

        if prev_tail is not None:
            prev_tail.next = new_head
        else:
            l = new_head
        prev_tail = current
        current = last
    return l
