"""
ou are part of a university admissions office and need to keep track of the kth highest test score from applicants
in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants
submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously
returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.

int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest
element in the pool of test scores so far.

T constructor: O(n log k)
T add(): O(log k)
S: O(k)
    - n is the size of the nums array.
    - k is the param and the size of the heap.
"""

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        heapq.heapify(self.nums)  # O(1) empty
        for num in nums:  # O(n)
            heapq.heappush(self.nums, num)  # O(k)

            if len(self.nums) > self.k:
                heapq.heappop(self.nums)  # O(k)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)  # O(log k)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)  # O(log k)

        return self.nums[0]  # O(1)


def test_kth_largest():
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8
