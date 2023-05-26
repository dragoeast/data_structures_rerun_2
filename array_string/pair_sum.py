def pair_sum(nums, target):
    """Return a tuple containing a pair of indices whose elements sum to the given target. 
    The indices returned must be unique.
    >>> pair_sum([4, 7, 9, 2, 5, 1], 3)
    (3, 5)
    """
    complement_dict = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in complement_dict:
            complement_index = complement_dict[complement]
            return (complement_index, index)
        else:
            complement_dict[number] = index
    
    return (-1, -1)
