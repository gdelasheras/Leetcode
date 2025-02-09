"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
It is guaranteed that the answer is unique.

T: O(N log K) N is the length of nums, K is the param
S: O(K)
"""

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)  # O(N)
        heap = []
        heapq.heapify(heap)

        for key, val in counter.items():  # O(K)
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


def test_topKFrequent():
    solution = Solution()
    assert set(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == set([1, 2])
    assert set(solution.topKFrequent([1], 1)) == set([1])
    assert set(solution.topKFrequent([1, 2], 2)) == set([1, 2])
    assert set(solution.topKFrequent(
        [1, 1, 3, 4, 5, 6, 7, 8, 9, 10], 1)) == set([1])
    assert set(solution.topKFrequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)) == set([
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
