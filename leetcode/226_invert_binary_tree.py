"""
Given the root of a binary tree, invert the tree, and return its root.

T: O(n)
S: O(n)

where:
    - n is the number of nodes in the tree.
"""

from typing import Optional
from utils.binary_tree import list_to_bst, bst_to_list_recursive


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(current_node):
            if not current_node:
                return None

            current_node.left, current_node.right = current_node.right, current_node.left

            invert(current_node.left)
            invert(current_node.right)

        invert(root)

        return root


def test_invert_tree():
    solution = Solution()
    assert bst_to_list_recursive(solution.invertTree(list_to_bst([1, 2, 3, 4, 5, 6, 7]))) == [
        7, 6, 5, 4, 3, 2, 1]
    assert bst_to_list_recursive(solution.invertTree(list_to_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))) == [
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert bst_to_list_recursive(solution.invertTree(list_to_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))) == [
        15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
