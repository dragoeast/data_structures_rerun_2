def five_sort(nums):
    """Rearrange elements of the list such that all 5s appear at the end.
    >>> five_sort(nums=[3, 6, 2, 5, 7, 5, 4])
    [3, 6, 2, 4, 7, 5, 5]
    >>> five_sort(nums=[2, 3, 6, 7, 5, 5, 5])
    [2, 3, 6, 7, 5, 5, 5]
    """
    l, r = 0, len(nums)-1
    while l < r:
        if nums[r] == 5:
            r -= 1
        elif nums[l] != 5:
            l += 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
    
    return nums
