"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

T: O(log N) N is the length of the array.
S: O(1) since we are not using any extra space.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (L+R) // 2
            if nums[M] == target:
                return M
            if nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        return -1


def test_search():
    s = Solution()
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert s.search([5], 5) == 0
    assert s.search([2, 5], 5) == 1
