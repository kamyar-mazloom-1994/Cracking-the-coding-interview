"""
Given a string, write a function to check if it's a permutation of a palindrome.
The palindrome does not have to be limited to dictionary words
"""


def pp_checker(string):
    # first remove the spaces in the string

    string = string.replace(" ", "")

    hashmap = {}
    for i in range(len(string)):
        if string[i] in hashmap:
            if hashmap[string[i]] == 1:
                hashmap[string[i]] -= 1
            else:
                hashmap[string[i]] += 1
        else:
            hashmap[string[i]] = 1

    hash_sum = sum(hashmap.values())

    if len(string) % 2 == 0 and hash_sum == 0:
        return True
    elif len(string) % 2 == 1 and hash_sum == 1:
        return True
    return False
