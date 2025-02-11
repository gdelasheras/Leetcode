"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Given a valid roman numeral, convert it to an integer.

T: O(n) n is the length of the string.
S: O(1) since the extra space is limited to 7.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        prev = table[s[0]]

        for i in range(1, len(s)):
            current = table[s[i]]
            if prev >= current:
                result += prev
            else:
                result -= prev
            prev = current
        result += prev
        return result


def test_romanToInt():
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    assert s.romanToInt("XL") == 40
    assert s.romanToInt("XC") == 90
    assert s.romanToInt("CD") == 400
    assert s.romanToInt("CM") == 900
    assert s.romanToInt("MMMCMXCIX") == 3999
