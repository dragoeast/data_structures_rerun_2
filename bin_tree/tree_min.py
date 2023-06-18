from node import Node


def tree_min_iter(root):
    """Return the minimum valueof the binary tree.
    BFS iterative version.
    >>> tree_min_iter(root=None) == float('inf')
    True
    >>> bin_tree = Node(10, Node(12), Node(5))
    >>> tree_min_iter(root=bin_tree)
    5
    """
    if root is None:
        return float('inf')

    min_value = float('inf')
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.val < min_value:
            min_value = curr.val

        for child in (curr.right, curr.left):
            if child is not None:
                stack.append(child)
    return min_value


def tree_min(root):
    """Return the minimum value of a binary tree.
    >>> tree_min(root=Node(5, Node(10), Node(3)))
    3
    """
    if root is None:
        return float('inf')

    left_min = tree_min(root.left)
    right_min = tree_min(root.right)

    return min(root.val, left_min, right_min)
