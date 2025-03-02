"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

T: O(n)
S: O(h)

where:
    - n is the number of nodes in the tree.
    - h is the height of the tree.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def diameter(curr_node):
            if not curr_node:
                return 0

            left_diameter = diameter(curr_node.left)
            right_diameter = diameter(curr_node.right)
            curr_diameter = left_diameter + right_diameter

            self.max_diameter = max(self.max_diameter, curr_diameter)

            return max(left_diameter, right_diameter) + 1

        diameter(root)

        return self.max_diameter


def test_diameterOfBinaryTree():
    s = Solution()
    assert s.diameterOfBinaryTree(TreeNode(1, TreeNode(
        2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3
    assert s.diameterOfBinaryTree(TreeNode(1, TreeNode(
        2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))) == 4
