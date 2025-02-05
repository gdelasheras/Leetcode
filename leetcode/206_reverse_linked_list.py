from typing import Optional

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

O(N) N is the number of nodes in the list.
S(1) since we are not using any extra space.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev = None
        while current_node:
            current_node.next, prev, current_node = prev, current_node, current_node.next
        return prev


def to_list(head: Optional[ListNode]) -> list:
    if not head:
        return []
    return [head.val] + to_list(head.next)


def test_reverseList():
    s = Solution()
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expected = [5, 4, 3, 2, 1]
    assert to_list(s.reverseList(lst)) == expected

    lst = ListNode(1, ListNode(2))
    expected = [2, 1]
    assert to_list(s.reverseList(lst)) == expected

    lst = None
    expected = []
    assert to_list(s.reverseList(lst)) == expected

    lst = ListNode(1)
    expected = [1]
    assert to_list(s.reverseList(lst)) == expected

    lst = ListNode(1, ListNode(2, ListNode(
        3, ListNode(4, ListNode(5, ListNode(6))))))
    expected = [6, 5, 4, 3, 2, 1]
    assert to_list(s.reverseList(lst)) == expected
