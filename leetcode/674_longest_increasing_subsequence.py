"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

T: O(n)
S: O(1)

where:
    - n is the length of the input array
"""
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        result, curr_rally = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curr_rally += 1
            else:
                curr_rally = 1
            result = max(result, curr_rally)
        return result


def test_findLengthOfLCIS():
    s = Solution()
    assert s.findLengthOfLCIS([1, 3, 5, 4, 7]) == 3
    assert s.findLengthOfLCIS([2, 2, 2, 2, 2]) == 1
    assert s.findLengthOfLCIS([1, 3, 5, 7, 9]) == 5
