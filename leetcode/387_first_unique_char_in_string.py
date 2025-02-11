"""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

T: O(n) n is the length of the string.
S: O(1) since it is limited to 26 characters.
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        return -1


def test_firstUniqChar():
    s = Solution()
    assert s.firstUniqChar("leetcode") == 0
    assert s.firstUniqChar("loveleetcode") == 2
    assert s.firstUniqChar("aabb") == -1
    assert s.firstUniqChar("a") == 0
    assert s.firstUniqChar("ab") == 0
    assert s.firstUniqChar("abc") == 0
    assert s.firstUniqChar("abac") == 1
    assert s.firstUniqChar("abacb") == 3
    assert s.firstUniqChar("abacbde") == 3
