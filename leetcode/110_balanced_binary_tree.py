"""
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

T: O(n)
T: O(h)

Where:
    - n is the number of nodes
    - h is the height of the tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True

        def dfs(current_node):
            if not current_node:
                return 0

            left_depth = dfs(current_node.left)
            right_depth = dfs(current_node.right)

            if abs(left_depth - right_depth) > 1:
                self.result = False

            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.result


def test_isBalanced():
    solution = Solution()
    assert solution.isBalanced(TreeNode(1, TreeNode(2), TreeNode(3))) == True
    assert solution.isBalanced(TreeNode(1, TreeNode(2), TreeNode(
        3, TreeNode(4), TreeNode(5, TreeNode(6))))) == False
