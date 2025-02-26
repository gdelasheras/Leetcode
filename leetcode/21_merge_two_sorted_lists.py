"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

T: O(n + m) 
S: O(1)

Where: 
    - n is the number of nodes in list 1
    - m is the number of nodes in list2
"""

from typing import Optional, List
from utils.linked_list import create_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        curr_result = dummy_head

        while list1 and list2:
            if list1.val < list2.val:
                curr_result.next = list1
                list1 = list1.next
            else:
                curr_result.next = list2
                list2 = list2.next
            curr_result = curr_result.next

        if list1:
            curr_result.next = list1

        if list2:
            curr_result.next = list2

        return dummy_head.next


def test_mergeTwoLists():
    s = Solution()
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = s.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]

    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = s.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == []

    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = s.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [0]
