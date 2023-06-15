class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def middle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    return slow.val


linked_list = Node('a', Node('b', Node('c', Node('d', Node('e')))))

print(f"{middle(head=linked_list) = }")
