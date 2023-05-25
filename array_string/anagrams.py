def anagrams(s1, s2):
    """Return a boolean indicating whether or not the strings are anagrams. 
    Anagrams are strings that contain the same characters, but in any order.
    >>> anagrams(s1="abcd", s2="bcda")
    True
    >>> anagrams(s1="abbcccd", s2="dcaccbb")
    True
    >>> anagrams(s1="abbcccd", s2="dcaccbbx")
    False
    """
    if len(s1) != len(s2):
        return False
    
    char_freq_s1 = _get_char_freq(s1)
    char_freq_s2 = _get_char_freq(s2)

    return char_freq_s1 == char_freq_s2

def _get_char_freq(s): 
    char_freq = {}

    for ch in s:
        if ch not in char_freq:
            char_freq[ch] = 0
        char_freq[ch] += 1

    return char_freq
