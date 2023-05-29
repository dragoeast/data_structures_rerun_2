class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def sum_list(head):
    """Return the sum of the values in the linked list.
    >>> sum_list(head=None)
    0
    >>> sum_list(head=Node(2, Node(3, Node(5))))
    10
    """
    if head is None:
        return 0
    
    return head.val + sum_list(head.next)
