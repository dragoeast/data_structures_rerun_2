class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def sum_list_iterative(head: Node) -> float:
    """Return the sum of the values in the linked list.
    >>> sum_list_iterative(head=None)
    0
    >>> sum_list_iterative(head=Node(2, Node(3, Node(5))))
    10
    >>> sum_list_iterative(head=Node(2.5, Node(3, Node(5.6))))
    11.1
    """
    total_sum = 0
    curr = head
    while curr is not None:
        total_sum += curr.val
        curr = curr.next

    return total_sum

def sum_list(head: Node) -> float:
    """Return the sum of the values in the linked list.
    >>> sum_list(head=None)
    0
    >>> sum_list(head=Node(2, Node(3, Node(5))))
    10
    """
    if head is None:
        return 0
    
    return head.val + sum_list(head.next)
