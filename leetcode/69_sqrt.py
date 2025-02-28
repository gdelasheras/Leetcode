"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

T: O(log x) being x the input.
S: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x

        while L <= R:
            M = (L+R)//2

            sqrt = M*M

            if sqrt == x:
                return M

            if sqrt < x:
                L = M+1
            else:
                R = M-1

        return R


def test_my_sqrt():
    solution = Solution()
    assert solution.mySqrt(4) == 2
    assert solution.mySqrt(8) == 2
    assert solution.mySqrt(16) == 4
    assert solution.mySqrt(25) == 5
    assert solution.mySqrt(0) == 0
    assert solution.mySqrt(1) == 1
    assert solution.mySqrt(2) == 1
    assert solution.mySqrt(3) == 1
    assert solution.mySqrt(5) == 2
    assert solution.mySqrt(6) == 2
    assert solution.mySqrt(7) == 2
