"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

T: O(n) n is the size of the linked list.
S: O(1)
"""

from typing import Optional
from utils.linked_list import create_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def test_middleNode():
    s = Solution()
    list = create_linked_list([1, 2, 3, 4, 5])
    result = s.middleNode(list)
    assert linked_list_to_list(result) == [3, 4, 5]

    list = create_linked_list([1, 2, 3, 4, 5, 6])
    result = s.middleNode(list)
    assert linked_list_to_list(result) == [4, 5, 6]
