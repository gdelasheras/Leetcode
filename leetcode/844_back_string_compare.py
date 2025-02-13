"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

T: O(n + m). Can also be O(max(n, m)), looking for the dominant term.
S: O(n + m)
    - n is the length of the string s.
    - t is the length of the string t.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            stack = []
            for c in string:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack

        return process(s) == process(t)


def test_backspaceCompare():
    s = Solution()
    assert s.backspaceCompare("ab#c", "ad#c") == True
    assert s.backspaceCompare("ab##", "c#d#") == True
    assert s.backspaceCompare("a#c", "ab") == False
    assert s.backspaceCompare("#", "") == True
    assert s.backspaceCompare("#", "####") == True
