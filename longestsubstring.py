from collections import OrderedDict


def length_of_longest_substring(s):
    '''
    Find length of longest substring of s with no repeating characters.

    Uses pointers i and j to search string, and an (ordered) dict to keep track
    of which letters have been seen.

    Initially i = 0, j = 1.

    1. j is then incremented until the character s[j] occurs in the substring
    s[i:j] -- i.e. we find the end of the non-repeating substring -- or until j
    == len(s). E.g. if s = 'abcabcda' then j is increased until i = 0, j = 3,
    and letters is a dict of 'abc'.

    2. s[i] is then removed from the dict letters, and i += 1 incremented. E.g.
    i = 1, j = 3, and letters contains 'bc'.

    j is then incremented again until a repeat or the end of the string (i.e.
    repeat 1), and then i is incremented again until i is within the length of
    the current candidate longest substring of the end of s, in which case you
    can stop looking.
    '''

    longest = 0

    # Use OrderedDict to preserve order, in case we ever want to return the
    # substing
    letters = OrderedDict()
    i = 0
    j = i

    while i < len(s) - longest:
        while j < len(s) and s[j] not in letters:
            letters[s[j]] = True
            j += 1

        if len(letters) > longest:
            longest = len(letters)

        del letters[s[i]]
        i += 1

    return longest


def length_of_longest_substring_slow(s):
    '''
    Find length of longest substring of s with no repeating characters (SLOW!)

    Uses pointers i and j to search string, and an (ordered) dict to keep track
    of which letters have been seen.

    Initially i = j = 0.

    For each i, increase j until you find a repeat or reach the end of the
    string. Make a note of the length of this substring if it is longer than
    the previously seen longest substring. Then increment i until it is within
    the length of the longest candidate substring of the end of s.
    '''
    longest = 0
    i = 0

    while i < len(s) - longest:

        letters = OrderedDict()
        j = i

        while j < len(s) and s[j] not in letters:
            letters[s[j]] = True
            j += 1

        if len(letters) > longest:
            longest = len(letters)

        i += 1

    return longest
