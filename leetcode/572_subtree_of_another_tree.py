"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

T: O(n + m)
S: O(n)

where:
    - n is the number of nodes in root.
    - m is the number of node in subRoot.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.serialized_trees = set()

        def serialize_tree(curr_node, save_in_hash=False):
            if not curr_node:
                return ""

            h = f"({curr_node.val},{serialize_tree(curr_node.left, save_in_hash)},{serialize_tree(curr_node.right, save_in_hash)})"

            if save_in_hash:
                self.serialized_trees.add(h)

            return h

        serialize_tree(root, True)
        serialized_sub_root = serialize_tree(subRoot)

        return serialized_sub_root in self.serialized_trees


def test_is_subtree():
    s = Solution()
    assert s.isSubtree(TreeNode(1, TreeNode(
        2), TreeNode(3)), TreeNode(2)) == True
    assert s.isSubtree(TreeNode(1, TreeNode(2), TreeNode(3)),
                       TreeNode(4)) == False
