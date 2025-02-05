"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

T: O(N) N is the length of numbers
S: O(1) We return the list, so the list is needed but no extra space required.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def pre_order(current_node):
            if not current_node:
                return

            self.result.append(current_node.val)
            pre_order(current_node.left)
            pre_order(current_node.right)
        self.result = []
        pre_order(root)
        return self.result


def test_preorderTraversal():
    s = Solution()

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert s.preorderTraversal(root) == [1, 2, 4, 5, 3]

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert s.preorderTraversal(root) == [1, 2, 4, 5, 3]

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert s.preorderTraversal(root) == [1, 2, 4, 5, 3]

    root = TreeNode(1)
    assert s.preorderTraversal(root) == [1]

    root = None
    assert s.preorderTraversal(root) == []

    root = TreeNode(1, TreeNode(2))
    assert s.preorderTraversal(root) == [1, 2]

    root = TreeNode(1, None, TreeNode(2))
    assert s.preorderTraversal(root) == [1, 2]

    root = TreeNode(1, TreeNode(2), None)
    assert s.preorderTraversal(root) == [1, 2]

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert s.preorderTraversal(root) == [1, 2, 3]
