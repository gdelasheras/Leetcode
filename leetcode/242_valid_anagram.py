"""
Given two strings s and t, return true if t is an  anagram of s, and false otherwise.

T: O(N) N is the length of the strings
S: O(1) since it is limited to 26 characters.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


def test_isAnagram():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat", "car") == False
    assert s.isAnagram("a", "ab") == False
    assert s.isAnagram("ab", "a") == False
    assert s.isAnagram("abc", "cba") == True
    assert s.isAnagram("abc", "abcd") == False
    assert s.isAnagram("abc", "abc") == True
    assert s.isAnagram("abc", "abcde") == False
    assert s.isAnagram("abc", "abcde") == False
    assert s.isAnagram("abc", "abcde") == False
