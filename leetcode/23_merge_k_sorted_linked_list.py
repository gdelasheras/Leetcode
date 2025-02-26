"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

T: O(n log k)
S: O(k) 

where:
    - n is the total number of nodes among all lists
    - k the number of lists.
"""

from typing import List, Optional
from utils.linked_list import create_linked_list, linked_list_to_list
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        heapq.heapify(nodes)

        for head in lists:
            if head:
                heapq.heappush(nodes, HeapNode(head))

        dummy = ListNode()
        current_new_node = dummy

        while nodes:
            current_smallest = heapq.heappop(nodes).node
            current_new_node.next = current_smallest
            current_new_node = current_new_node.next

            if current_smallest.next:
                heapq.heappush(nodes, HeapNode(current_smallest.next))

        return dummy.next


def test_mergeKLists():
    s = Solution()
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6]),
    ]

    result = s.mergeKLists(lists)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]

    lists = [
        create_linked_list([]),
        create_linked_list([3]),
        create_linked_list([1, 2, 4]),
    ]
    result = s.mergeKLists(lists)
    assert linked_list_to_list(result) == [1, 2, 3, 4]
