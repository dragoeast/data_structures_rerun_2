from node import Node


def tree_includes(root, target):
    """Return True if target is in the binary tree.
    False otherwise.
    >>> tree_includes(root=None, target=42)
    False
    >>> tree_includes(root=Node(5), target=5)
    True
    >>> tree_includes(root=Node(5), target=42)
    False
    >>> tree_includes(root=Node(5), target=5)
    True
    >>> bin_tree = Node(10, Node(5, Node(2), Node(8)), Node(20, right=Node(100)))
    >>> tree_includes(root=bin_tree, target=8)
    True
    >>> tree_includes(root=bin_tree, target=7)
    False
    """
    if root is None:
        return False
    
    if root.val == target:
        return True
    
    left_include  = tree_includes(root.left, target)
    right_include = tree_includes(root.right, target)

    return left_include or right_include
