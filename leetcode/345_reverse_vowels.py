"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

T: O(n)
S: O(n)

where:
    - n is the length of the input string
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        L, R = 0, len(s)-1

        vowels = {'a', 'e', 'i', 'o', 'u'}

        while L < R:
            if s[L].lower() in vowels and s[R].lower() in vowels:
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1
            elif s[L].lower() not in vowels:
                L += 1
            else:
                R -= 1

        return ''.join(s)


def test_reverseVowels():
    s = Solution()
    assert s.reverseVowels("hello") == "holle"
    assert s.reverseVowels("leetcode") == "leotcede"
    assert s.reverseVowels("aA") == "Aa"
