"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        current_node = dummy_head
        next_sum = 0
        while l1 or l2:

            local_sum = next_sum
            if l1:
                local_sum += l1.val
                l1 = l1.next

            if l2:
                local_sum += l2.val
                l2 = l2.next

            if local_sum >= 10:
                local_sum, next_sum = local_sum % 10, 1
            else:
                local_sum, next_sum = local_sum, 0
            current_node.next = ListNode(local_sum)
            current_node = current_node.next

        if next_sum > 0:
            current_node.next = ListNode(next_sum)

        return dummy_head.next


def test_addTwoNumbers():
    s = Solution()
    result = s.addTwoNumbers(create_linked_list(
        [2, 4, 3]), create_linked_list([5, 6, 4]))
    assert linked_list_to_list(result) == [7, 0, 8]

    result = s.addTwoNumbers(create_linked_list([0]), create_linked_list([0]))
    assert linked_list_to_list(result) == [0]
    result = s.addTwoNumbers(create_linked_list(
        [9, 9]), create_linked_list([9, 9, 9, 9, 9]))
    assert linked_list_to_list(result) == [8, 9, 0, 0, 0, 1]
