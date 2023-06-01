class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def get_values(root):
    """Return the values of a depth first search traverse as a list.
    >>> root = Node('a', Node('b', Node('d'), Node('e')), Node('c', right = Node('f')))
    >>> get_values(root)
    ['a', 'b', 'd', 'e', 'c', 'f']
    >>> get_values(root=None)
    []
    """
    if root is None:
        return []
    
    values = []
    stack = [ root ]
    while stack:
        curr = stack.pop()
        values.append(curr.val)

        for child in (curr.right, curr.left):
            if child is not None:
                stack.append(child)
    
    return values
