# index         0123456
# uncompress(s="2c3a1t")
#                j
#               i

def uncompress(s):
    """Return an uncompressed version of the string,
    where each 'char' of a group is repeated 'number' times consecutively
    Time: O(n), Space: O(n)
    >>> uncompress(s="2c3a1t")
    'ccaaat'
    >>> uncompress(s="2c13a1t4d")
    'ccaaaaaaaaaaaaatdddd'
    """
    uncompressed_lst = []
    digits = "0123456789"
    i, j = 0, 0
    while i < len(s):
        if s[j] in digits:
            j += 1
        else:
            char = s[j]
            times = int(s[i:j])
            uncompressed_lst.append(f"{char * times}" if times > 1 else f"{char}")
            j += 1
            i = j

    return ''.join(uncompressed_lst)
