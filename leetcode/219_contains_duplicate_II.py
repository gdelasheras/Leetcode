"""
Given an integer array nums and an integer k, return true if there are two distinct 
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

T: O(N) N is the length of nums
S: O(min(N, K)) K is the number of unique elements in nums
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        for index, num in enumerate(nums):
            if num in visited:
                return True

            visited.add(num)

            if len(visited) > k:
                visited.remove(nums[index-k])

        return False


def test_containsNearbyDuplicate():
    s = Solution()
    assert s.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
    assert s.containsNearbyDuplicate([1, 1, 2, 3, 4], 1) == True
    assert s.containsNearbyDuplicate([1, 3, 2, 3, 4], 1) == False
    assert s.containsNearbyDuplicate([1], 1) == False
    assert s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
