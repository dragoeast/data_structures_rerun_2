from node import Node

def linked_list_find_iterative(head, target):
    """Return True if target is in the linked list.
    False otherwise.
    >>> linked_list_find_iterative(head=None, target=3)
    False
    >>> linked_list_find_iterative(head=Node(3), target=3)
    True
    >>> linked_list_find_iterative(head=Node(2, Node(5, Node(7, Node(3)))), target=3)
    True
    >>> linked_list_find_iterative(head=Node(2, Node(5, Node(7, Node(3)))), target=11)
    False
    """
    if head is None:
        return False
    
    curr = head
    while curr is not None:
        if curr.val == target:
            return True
        curr = curr.next
    
    return False


def linked_list_find(head, target):
    """Return True if target is in the linked list.
    False otherwise.
    >>> linked_list_find(head=None, target=3)
    False
    >>> linked_list_find(head=Node(3), target=3)
    True
    >>> linked_list_find(head=Node(2, Node(5, Node(7, Node(3)))), target=3)
    True
    >>> linked_list_find(head=Node(2, Node(5, Node(7, Node(3)))), target=11)
    False
    """
    if head is None:
        return False
    
    match = head.val == target

    return match or linked_list_find(head.next, target)
