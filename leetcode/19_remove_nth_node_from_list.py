"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

T: O(n) being n the number of nodes in the linked list.
S: O(1)
"""

from typing import Optional
from utils.linked_list import create_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        first = dummy_head
        second = dummy_head

        for _ in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy_head.next


def test_removeNthFromEnd():
    s = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    result = s.removeNthFromEnd(head, 2)
    assert linked_list_to_list(result) == [1, 2, 3, 5]

    head = create_linked_list([1])
    result = s.removeNthFromEnd(head, 1)
    assert linked_list_to_list(result) == []

    head = create_linked_list([1, 2])
    result = s.removeNthFromEnd(head, 1)
    assert linked_list_to_list(result) == [1]
