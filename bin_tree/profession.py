def profession(level, position):
    """Consider a special family of Engineers and Doctors. This family has the following rules:

        -Everybody has two children.
        -The first child of an Engineer is an Engineer and the second child is a Doctor.
        -The first child of a Doctor is a Doctor and the second child is an Engineer.
        -All generations of Doctors and Engineers start with an Engineer.

    Return the profession of a person in a family tree at the specific level and position.
    >>> profession(level=1, position=1)
    'Engineer'
    >>> [ profession(level=2, position=pos) for pos in range(1, 2+1) ]
    ['Engineer', 'Doctor']
    >>> [ profession(level=3, position=pos) for pos in range(1, 4+1) ]
    ['Engineer', 'Doctor', 'Doctor', 'Engineer']
    >>> [ profession(level=4, position=pos) for pos in range(1, 8+1) ]
    ['Engineer', 'Doctor', 'Doctor', 'Engineer', 'Doctor', 'Engineer', 'Engineer', 'Doctor']
    """
    return "Engineer" if _profession(level, position) == True else "Doctor"


def _profession(level, position):
    if level == 1:
        return True

    parent_position = (position+1) // 2
    parent = _profession(level-1, parent_position)
    odd_position = position % 2 == 1

    return parent if odd_position else not parent
