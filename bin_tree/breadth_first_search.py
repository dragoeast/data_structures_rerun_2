from collections import deque
from node import Node


def breadth_first_search(root):
    """Return the BFS traverse values as a list of the binary tree.
    >>> bin_tree = Node('a', Node('b', Node('d'), Node('e')), Node('c', right=Node('f')))
    >>> breadth_first_search(root=bin_tree)
    ['a', 'b', 'c', 'd', 'e', 'f']
    """
    if root is None:
        return []
    
    value_lst = []
    queue = deque( [ root ] )
    while queue:
        curr = queue.popleft()
        value_lst.append(curr.val)

        for child in (curr.left, curr.right):
            if child is not None:
                queue.append(child)
    
    return value_lst
