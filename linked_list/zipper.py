from node import Node
from values import get_values
from create_linked_list import create_linked_list

def zipper(head_1: Node, head_2: Node) -> Node:
    """Zipper the two lists together into single linked list by alternating nodes.
    If one of the linked lists is longer than the other, 
    the resulting list should terminate with the remaining nodes. 
    The function should return the head of the zippered linked list.
    >>> head_1 = create_linked_list(values=[ value for value in "abc" ])
    >>> head_2 = create_linked_list(values=[ value for value in "xyz" ])
    >>> zipped_head = zipper(head_1, head_2)
    >>> get_values(head=zipped_head)
    ['a', 'x', 'b', 'y', 'c', 'z']
    >>> head_1 = create_linked_list(values=[ value for value in "abcd" ])
    >>> head_2 = create_linked_list(values=[ value for value in "xyz" ])
    >>> zipped_head = zipper(head_1, head_2)
    >>> get_values(head=zipped_head)
    ['a', 'x', 'b', 'y', 'c', 'z', 'd']
    """
    tail = head_1
    curr_1, curr_2 = head_1.next, head_2
    counter = 0
    while curr_1 and curr_2:
        if counter % 2 == 0:
            tail.next = curr_2
            curr_2 = curr_2.next
        else:
            tail.next = curr_1
            curr_1 = curr_1.next
        counter += 1
        tail = tail.next
    
    if curr_1:
        tail.next = curr_1
    if curr_2:
        tail.next = curr_2
    
    return head_1
