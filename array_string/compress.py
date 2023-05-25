# index     0123456789
# compress('ccaaatsss*') # -> '2c3at3s'
#                    j
#                    i

def compress(s):
    """Return a compressed version of the string,
      where consecutive occurrences of the same characters are compressed 
      into the number of occurrences followed by the character.
    >>> compress(s='ccaaatsss')
    '2c3at3s'
    """
    compressed_str = ""
    s += '*'
    i, j = 0, 0
    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
            times = j - i
            char = s[i]
            compressed_str += str(times) + char if times > 1 else char
            i = j
    return compressed_str
