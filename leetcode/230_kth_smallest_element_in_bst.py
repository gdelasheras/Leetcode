"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

T: O(k)
S: O(h)

where:
    - n is the number of nodes in the tree
    - h is the height of the tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = 0
        self.k = k

        def dfs(curr_node):
            if self.k == 0 or not curr_node:
                return

            dfs(curr_node.left)

            self.k -= 1
            if self.k == 0:
                self.result = curr_node.val

            dfs(curr_node.right)

        dfs(root)
        return self.result


def test_kth_smallest():
    s = Solution()
    assert s.kthSmallest(TreeNode(2, TreeNode(1), TreeNode(3)), 1) == 1
    assert s.kthSmallest(TreeNode(2, TreeNode(1), TreeNode(3)), 2) == 2
    assert s.kthSmallest(TreeNode(2, TreeNode(1), TreeNode(3)), 3) == 3
