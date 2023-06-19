from node import Node


def max_path_sum(root):
    """Return the max path sum from the root to the leafs.
    >>> bin_tree = Node(10, Node(5, Node(1), Node(100)), Node(20, right=Node(25)))
    >>> max_path_sum(root=bin_tree)
    115
    """
    if root is None:
        return float('-inf')
    if _leaf(root):
        return root.val

    left_path_sum = max_path_sum(root.left)
    right_path_sum = max_path_sum(root.right)

    return root.val + max(left_path_sum, right_path_sum)


def _leaf(node): return node.left is None and node.right is None
