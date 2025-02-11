"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

T: O(n) n is the length of s
S: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if not s[L].isalnum():
                L += 1
                continue

            if not s[R].isalnum():
                R -= 1
                continue

            if s[L].lower() != s[R].lower():
                return False

            L += 1
            R -= 1

        return True


def test_isPalindrome():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False
    assert s.isPalindrome(" ") == True
    assert s.isPalindrome("") == True
    assert s.isPalindrome("a") == True
    assert s.isPalindrome("12321") == True
    assert s.isPalindrome("123a321") == True
    assert s.isPalindrome("RealMadrid") == False
