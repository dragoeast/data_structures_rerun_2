class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def get_values_iterative(head: Node) -> list:
    """Return a list of the values in the linked list.
    This implementation is iterative.
    >>> get_values_iterative(head=None)
    []
    >>> get_values_iterative(head=Node('a', Node('b', Node('c'))))
    ['a', 'b', 'c']
    """
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next

    return values

def get_values(head: Node) -> list:
    """Return a list of the values in the linked list.
    >>> get_values(head=None)
    []
    >>> get_values(head=Node('a', Node('b', Node('c'))))
    ['a', 'b', 'c']
    """
    values = []
    _get_values(head, values)

    return values

def _get_values(head: Node, values: list) -> None:
    """Recursive helper function to update the values list 
    while stepping through the linked list."""
    if head is None:
        return
    
    values.append(head.val)
    _get_values(head.next, values)
