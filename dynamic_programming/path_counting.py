def count_paths(grid):
    """Return the number of path possible from the upper left corner to the bottom right corner
    without hitting the wall. 'X' represents walls in the grid. It is possible to move only down or to the right.
    >>> grid = [\
        ['O', 'O', 'X',],\
        ['O', 'O', 'O',],\
        ]
    >>> count_paths(grid)
    2
    """
    return _count_paths(grid, row=0, col=0)


def _count_paths(grid, row, col):
    if not _inbound(grid, row, col) or _wall(grid, row, col):
        return 0
    if _bottom_right(grid, row, col):
        return 1

    down_count = _count_paths(grid, row+1, col)
    right_count = _count_paths(grid, row, col+1)

    return down_count + right_count


def _inbound(grid, row, col):
    row_inbound = row in range(0, len(grid))
    col_inbound = col in range(0, len(grid[0]))

    return row_inbound and col_inbound


def _wall(grid, row, col):
    return grid[row][col] == 'X'


def _bottom_right(grid, row, col):
    return row == len(grid)-1 and col == len(grid[0])-1
