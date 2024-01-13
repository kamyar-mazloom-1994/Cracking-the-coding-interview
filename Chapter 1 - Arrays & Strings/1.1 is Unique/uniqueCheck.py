"""
Implement an algorithm to determine if a string has all unique characters
"""


def unique_check(string) -> bool:
    # assume ASCII character set
    if len(string) >= 256:
        return False

    hashmap = {}
    for i in range(len(string)):
        if string[i] in hashmap:
            return False
        hashmap[string[i]] = i
    return True
