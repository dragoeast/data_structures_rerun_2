def _pair_operation(items, target, func):
    complement_dict = {}
    for index, item in enumerate(items):
        complement = func(target, item)
        if complement in complement_dict:
            complement_index = complement_dict[complement]
            return (complement_index, index)
        else:
            complement_dict[item] = index
    
    return (-1, -1)

def pair_product(nums, target):
    """Return a tuple containing a pair of indices whose elements multiply to the given target.
      The indices returned must be unique.
    >>> pair_product(nums=[4, 7, 9, 2, 5, 1], target=5)
    (4, 5)
    >>> pair_product(nums=[4, 7, 9, 2, 5, 1], target=11)
    (-1, -1)
    """
    return _pair_operation(items=nums, target=target, func=lambda x, y: x / y)

def pair_sum(nums, target):
    """Return a tuple containing a pair of indices whose elements sum to the given target. 
    The indices returned must be unique.
    >>> pair_sum([4, 7, 9, 2, 5, 1], 3)
    (3, 5)
    """
    return _pair_operation(items=nums, target=target, func=lambda a, b: a - b)
