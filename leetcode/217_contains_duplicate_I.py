"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

T: O(N) N is the length of nums
S: O(K) K is the number of unique elements in nums
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False


def test_containsDuplicate():
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 4]) == False
    assert s.containsDuplicate([1, 4, 3, 4]) == True
    assert s.containsDuplicate([1]) == False
    assert s.containsDuplicate([]) == False
