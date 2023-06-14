from node import Node


def symmetric_tree(root):
    """Return True if the binary treeis symmetric.
    False otherwise.
    >>> bin_tree = Node('a', Node('b', Node('c', right=Node('d'))), Node('b', right=Node('c', left=Node('d'))))
    >>> symmetric_tree(root=bin_tree)
    True
    >>> symmetric_tree(root=Node('a'))
    True
    >>> symmetric_tree(root=None)
    True
    >>> bin_tree = Node('a', Node('b', Node('c', right=Node('e'))), Node('b', right=Node('c', left=Node('d'))))
    >>> symmetric_tree(root=bin_tree)
    False
    """
    return _symmetric_tree(left=root, right=root)


def _symmetric_tree(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False

    return left.val == right.val and _symmetric_tree(left.left, right.right) and _symmetric_tree(left.right, right.left)
