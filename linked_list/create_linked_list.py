from node import Node
from values import get_values

def create_linked_list(values):
    """Create and return the head of the linked list populated from the values list
    >>> head = create_linked_list(values=[2, 3, 4])
    >>> get_values(head)
    [2, 3, 4]
    >>> head = create_linked_list(values=[])
    >>> get_values(head)
    []
    """
    fake_head = Node(42)
    curr = fake_head
    for number in values:
        curr.next = Node(number)
        curr = curr.next

    return fake_head.next
