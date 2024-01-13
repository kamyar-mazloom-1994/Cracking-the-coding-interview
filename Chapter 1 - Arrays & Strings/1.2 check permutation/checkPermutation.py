"""
Given two strings write a function to check if one is a permutation of the other
"""


def check_permutation(string1, string2):
    # check size difference

    if len(string1) != len(string2):
        return False

    hashmap = {}
    for i in range(len(string1)):
        if string1[i] in hashmap:
            hashmap[string1[i]] += 1
        else:
            hashmap[string1[i]] = 1

    for j in range(len(string2)):
        if string2[j] in hashmap and hashmap[string2[j]] > 0:
            hashmap[string2[j]] -= 1
        else:
            return False
    return True
