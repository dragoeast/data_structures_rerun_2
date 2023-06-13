def max_path_sum(grid):
    """Return the max path sum from the upper left corner
    to the bottom right corner.
    >>> grid = [\
        [1, 3, 12],\
        [5, 1, 1],\
        [3, 6, 1],\
    ]
    >>> max_path_sum(grid)
    18
    """
    return _max_path_sum(grid, row=0, col=0)


def _max_path_sum(grid, row, col):
    if not _inbound(grid, row, col):
        return 0
    if _bottom_right(grid, row, col):
        return grid[row][col]

    down_path_sum = _max_path_sum(grid, row+1, col)
    right_path_sum = _max_path_sum(grid, row, col+1)

    return grid[row][col] + max(down_path_sum, right_path_sum)


def _inbound(grid, row, col):
    row_inbound = row in range(0, len(grid))
    col_inbound = col in range(0, len(grid[0]))

    return row_inbound and col_inbound


def _bottom_right(grid, row, col):
    return row == len(grid)-1 and col == len(grid[0])-1
