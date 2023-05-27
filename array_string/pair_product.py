def pair_product(nums, target):
    """return a tuple containing a pair of indices whose elements multiply to the given target.
      The indices returned must be unique.
    >>> pair_product(nums=[4, 7, 9, 2, 5, 1], target=5)
    (4, 5)
    >>> pair_product(nums=[4, 7, 9, 2, 5, 1], target=11)
    (-1, -1)
    """
    complement_dict = {}
    for index, number in enumerate(nums):
        complement = target / number
        if complement in complement_dict:
            complement_index = complement_dict[complement]
            return (complement_index, index)
        else:
            complement_dict[number] = index
    
    return (-1, -1)
