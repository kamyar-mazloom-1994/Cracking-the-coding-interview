"""
Assume you have a method isSubstring which checks if one word is a substring of another. Given
two strings s1 and s2 write a check to see if s2 is a rotation of s1 using only one isSubstring
"""


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False
