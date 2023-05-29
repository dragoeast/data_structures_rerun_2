from node import Node
from typing import Optional

def get_node_value(head: Node, index: int) -> Optional[int] :
    """Return the value at the index in the linked list.
    If the linked list is shorter than the index, then return None.
    >>> get_node_value(head=Node(2, Node(3)), index=-1) is None
    True
    >>> get_node_value(head=Node(2, Node(3)), index=0)
    2
    >>> get_node_value(head=Node(2, Node(3)), index=1)
    3
    >>> get_node_value(head=Node(2, Node(3)), index=5) is None
    True
    """
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value(head.next, index-1)
