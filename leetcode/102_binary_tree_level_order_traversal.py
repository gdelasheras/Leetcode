"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

T: O(n)
S: O(n)

where:
    - n is the number of nodes in the tree.
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                curr_node = queue.popleft()

                level.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

            result.append(level)
        return result


def test_level_order():
    s = Solution()
    assert s.levelOrder(TreeNode(1, TreeNode(2), TreeNode(3))) == [[1], [2, 3]]
    assert s.levelOrder(TreeNode(1, TreeNode(2), TreeNode(
        3, TreeNode(4), TreeNode(5)))) == [[1], [2, 3], [4, 5]]
    assert s.levelOrder(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(
        4), TreeNode(5, TreeNode(6))))) == [[1], [2, 3], [4, 5], [6]]
