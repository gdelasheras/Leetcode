"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_max = float('-inf')
            for _ in range(len(queue)):
                curr_node = queue.popleft()

                level_max = max(curr_node.val, level_max)

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

            result.append(level_max)
        return result


def test_largest_values():
    s = Solution()
    assert s.largestValues(TreeNode(1, TreeNode(3, TreeNode(
        5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))) == [1, 3, 9]
    assert s.largestValues(TreeNode(1, TreeNode(2), TreeNode(3))) == [1, 3]
    assert s.largestValues(TreeNode(1, TreeNode(2), TreeNode(
        3, TreeNode(4), TreeNode(5)))) == [1, 3, 5]
    assert s.largestValues(TreeNode(1, TreeNode(2), TreeNode(
        3, TreeNode(4), TreeNode(5, TreeNode(6))))) == [1, 3, 5, 6]
