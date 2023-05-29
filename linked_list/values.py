class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def get_values(head):
    """Return a list of the values in the linked list.
    >>> get_values(head=None)
    []
    >>> get_values(head=Node('a', Node('b', Node('c'))))
    ['a', 'b', 'c']
    """
    values = []
    _get_values(head, values)

    return values

def _get_values(head, values):
    """Recursive helper function to update the values list 
    while stepping through the linked list."""
    if head is None:
        return
    
    values.append(head.val)
    _get_values(head.next, values)
