"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

T: O(n)
S: O(n)

where:
    - n is the number of nodes in the tree
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_vals = []
            for _ in range(len(queue)):
                curr_node = queue.popleft()

                level_vals.append(curr_node.val)

                if curr_node.right:
                    queue.append(curr_node.right)

                if curr_node.left:
                    queue.append(curr_node.left)

            result.append(level_vals[0])
        return result


def test_right_side_view():
    s = Solution()
    assert s.rightSideView(TreeNode(1, TreeNode(2), TreeNode(3))) == [1, 3]
    assert s.rightSideView(TreeNode(1, TreeNode(2), TreeNode(
        3, TreeNode(4), TreeNode(5)))) == [1, 3, 5]
    assert s.rightSideView(TreeNode(1, TreeNode(2), TreeNode(
        3, TreeNode(4), TreeNode(5, TreeNode(6))))) == [1, 3, 5, 6]
