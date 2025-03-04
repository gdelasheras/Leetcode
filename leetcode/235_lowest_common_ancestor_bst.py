"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as 
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).

T: O(h)
S: O(1)

where:
    - h is the height of the tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return self.val == other.val


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_node = root
        while curr_node:
            if p.val < curr_node.val and q.val < curr_node.val:
                curr_node = curr_node.left
            elif p.val > curr_node.val and q.val > curr_node.val:
                curr_node = curr_node.right
            else:
                return curr_node


def test_lowestCommonAncestor():
    s = Solution()
    assert s.lowestCommonAncestor(TreeNode(2, TreeNode(1), None), TreeNode(
        2), TreeNode(1)) == TreeNode(2)
