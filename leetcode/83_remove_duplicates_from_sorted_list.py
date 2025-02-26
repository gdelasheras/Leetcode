"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

T: O(n) n is the number of nodes in the linked list
S: O(1)
"""

from typing import Optional
from utils.linked_list import create_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return head


def test_deleteDuplicates():
    s = Solution()
    list = create_linked_list([1, 1, 2])
    result = s.deleteDuplicates(list)
    assert linked_list_to_list(result) == [1, 2]
    print("---")
    list = create_linked_list([1, 1, 2, 3, 3])
    result = s.deleteDuplicates(list)
    assert linked_list_to_list(result) == [1, 2, 3]

    list = create_linked_list([])
    result = s.deleteDuplicates(list)
    assert linked_list_to_list(result) == []
