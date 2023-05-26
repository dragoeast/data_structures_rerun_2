def most_freq_char(s):
    """Return the most frequent character of the string. If there are ties, 
    return the character that appears earlier in the string.
    >>> most_freq_char(s="mississippi")
    'i'
    """
    char_freq = _get_char_freq(s)

    max_freq = 0
    max_freq_ch = None
    for ch in s:
        curr_freq = char_freq[ch]
        if curr_freq > max_freq:
            max_freq = curr_freq
            max_freq_ch = ch
    
    
    return max_freq_ch

def _get_char_freq(s):
    char_freq = {}

    for ch in s:
        if ch not in char_freq:
            char_freq[ch] = 0
        char_freq[ch] += 1

    return char_freq
