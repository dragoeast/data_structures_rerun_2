from node import Node


def reverse(head):
    """Reverse and return the new head of the linked list.
    >>> reverse(head=None) is None
    True
    >>> reversed_head = reverse(head=Node(2, Node(3, Node(5))))
    >>> reversed_head.val
    5
    """
    prev, curr = None, head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev
