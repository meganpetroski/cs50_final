from nltk.tokenize import sent_tokenize, word_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # Split strings into sets of lines
    lines1 = set(a.splitlines())
    lines2 = set(b.splitlines())

    # Intersect sets
    return list(lines1.intersection(lines2))


def sentences(a, b):
    """Return sentences in both a and b"""

    # Tokenize strings
    tokens1 = set(sent_tokenize(a))
    tokens2 = set(sent_tokenize(b))

    # Intersect sets
    return list(tokens1.intersection(tokens2))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # Sets of unique substrings of length n
    substrings1 = _substrings(a, n)
    substrings2 = _substrings(b, n)

    # Intersect sets
    intersection = substrings1.intersection(substrings2)

    # Return as list
    return list(intersection)


def _substrings(s, n):
    """Return set of substrings of s, each of length n."""

    # Return substrings of length i
    substrings = set()
    for i in range(len(s) - n + 1):
        substrings.add(s[i:i + n])
    return substrings
