from node import Node


def tree_sum(root):
    """Return the sum of the values in the binary tree root.
    >>> bin_tree = Node(3)
    >>> tree_sum(root=bin_tree)
    3
    >>> bin_tree = Node(2, Node(3, Node(7), Node(11)), Node(5, right=Node(13)))
    >>> tree_sum(root=bin_tree)
    41
    >>> tree_sum(root=None)
    0
    """
    if root is None:
        return 0
    
    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)

    return root.val + left_sum + right_sum
