"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

T: O(N) N is the length of s
S: O(N) N is the length of s
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        for char in s:
            if char not in symbols.keys():
                stack.append(char)
            else:
                if stack and stack[-1] == symbols[char]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False


def test_isValid():
    solution = Solution()
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid("{[]}") == True
