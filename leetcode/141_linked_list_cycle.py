"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 

Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

T: O(n) being n the number of nodes in the linked list.
S: O(1)
"""

from typing import Optional
from utils.linked_list import create_linked_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False


def test_hasCycle():
    s = Solution()
    list1 = create_linked_list([3, 2, 0, -4])
    list1.next.next.next.next = list1.next
    assert s.hasCycle(list1) == True

    list2 = create_linked_list([1, 2])
    list2.next.next = list2
    assert s.hasCycle(list2) == True

    list3 = create_linked_list([1])
    assert s.hasCycle(list3) == False
