"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

T: O(n log k)
S: O(k)
    - n is the size of the list
    - k is the parameter
"""
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)  # O(1) empty

        for num in nums:  # O(n)
            heapq.heappush(heap, num)  # O(k)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]  # O(1)


def test_findKthLargest():
    s = Solution()
    assert s.findKthLargest([7, 2, 0, 4, 5, 6], 2) == 6
    assert s.findKthLargest([7, 2, 0, 4, 5, 6], 1) == 7
