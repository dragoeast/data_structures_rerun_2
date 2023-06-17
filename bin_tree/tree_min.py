from node import Node


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
