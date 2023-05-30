from node import Node
from create_linked_list import create_linked_list
from values import get_values

def merge(head_1, head_2):
    """Merge two sorted linked lists in place.
    Return the head of the merged linked list.
    >>> head_1 = create_linked_list(values=[1, 5, 6, 10])
    >>> head_2 = create_linked_list(values=[2, 3, 4, 7, 12])
    >>> merged_head = merge(head_1, head_2)
    >>> get_values(head=merged_head)
    [1, 2, 3, 4, 5, 6, 7, 10, 12]
    """
    fake_head = Node(42)
    tail = fake_head
    curr_1, curr_2 = head_1, head_2
    while curr_1 is not None and curr_2 is not None:
        if curr_1.val <= curr_2.val:
            tail.next = curr_1
            curr_1 = curr_1.next
        else:
            tail.next = curr_2
            curr_2 = curr_2.next
        tail = tail.next
    
    if curr_1 is not None:
        tail.next = curr_1
    if curr_2 is not None:
        tail.next = curr_2
    
    return fake_head.next
