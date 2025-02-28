"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

T: O(min(n1, n2))  Stops early when one tree is shorter.
S: O(min(h1, h2)) stack calls

Where:
    - n1: number of nodes of the first tree.
    - n2: number of nodes of the second tree.
    - h1: height of the first tree.
    - h2: height of the second tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def same_tree(current_node_tree1, current_node_tree2):
            if not current_node_tree1 and not current_node_tree2:
                return True

            if not current_node_tree1 or not current_node_tree2:
                return False

            if current_node_tree1.val != current_node_tree2.val:
                return False

            return same_tree(current_node_tree1.left, current_node_tree2.left) and same_tree(current_node_tree1.right, current_node_tree2.right)

        return same_tree(p, q)


def test_isSameTree():
    solution = Solution()
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(
        3)), TreeNode(1, TreeNode(2), TreeNode(3))) == True
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(
        3)), TreeNode(1, TreeNode(2), TreeNode(4))) == False
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(
        3)), TreeNode(1, TreeNode(2), TreeNode(3))) == True
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(
        3)), TreeNode(1, TreeNode(2), TreeNode(3))) == True
    assert solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(
        3)), TreeNode(1, TreeNode(2), TreeNode(3))) == True
