"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

T: O(n log n)
S: O(n)
"""
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]  # O(n)
        heapq.heapify(stones)  # O(n)

        while len(stones) > 1:  # O(n)
            stone_1 = -heapq.heappop(stones)  # O(log n)
            stone_2 = -heapq.heappop(stones)  # O(log n)

            if stone_1 > stone_2:
                new_stone = stone_1 - stone_2
                heapq.heappush(stones, -new_stone)  # O(log n)

        return -heapq.heappop(stones) if stones else 0  # O(1)


def test_last_stone_weight():
    solution = Solution()
    assert solution.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert solution.lastStoneWeight([1]) == 1
    assert solution.lastStoneWeight([1, 1]) == 0
    assert solution.lastStoneWeight([1, 2]) == 1
    assert solution.lastStoneWeight([1, 2, 3]) == 0
