"""
Implement a method that performs a basic string compression using the counts of repeated characters.
If the compressed characters are longer return the original string.

Ex. aabcccccaaa => a2b1c5a3
"""


def string_compression(s1):
    s2 = ""
    count = 1

    for i in range(0, len(s1) - 1):
        if s1[i] == s1[i + 1]:
            i += 1
            count += 1
        else:
            s2 += s1[i] + str(count)
            count = 1

    s2 += s1[len(s1) - 1] + str(count)

    if len(s2) < len(s1):
        return s2
    return s1
