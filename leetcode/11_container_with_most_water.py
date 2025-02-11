"""
You are given an integer array height of length n. 

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

T: O(n) n is the length of the array.
S: O(1) since we are not using any extra space.
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calculate_area(left, right, h):
            return (right - left) * h

        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            shortest_h = min(height[left], height[right])
            result = max(result, calculate_area(left, right, shortest_h))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result


def test_maxArea():
    s = Solution()
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([1, 2, 3, 4]) == 4
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert s.maxArea([10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 100
