"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

T: O(n)
T: O(h)

Where:
    - n is the number of nodes
    - h is the height of the tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(current_node):
            if not current_node:
                return 0

            return max(dfs(current_node.left), dfs(current_node.right)) + 1

        return dfs(root)


def test_max_depth():
    solution = Solution()
    assert solution.maxDepth(TreeNode(1, TreeNode(2), TreeNode(3))) == 2
    assert solution.maxDepth(
        TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))) == 3
