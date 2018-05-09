from nltk.tokenize import sent_tokenize, word_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # Split strings into sets of lines
    lines1 = set(a.splitlines())
    lines2 = set(b.splitlines())

    # Intersect sets
    return list(lines1.intersection(lines2))
