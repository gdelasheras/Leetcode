"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

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
    def isSymmetric(self, root: TreeNode) -> bool:
        def same_tree(current_node_tree1, current_node_tree2):
            if not current_node_tree1 and not current_node_tree2:
                return True

            if not current_node_tree1 or not current_node_tree2:
                return False

            if current_node_tree1.val != current_node_tree2.val:
                return False

            return same_tree(current_node_tree1.left, current_node_tree2.right) and same_tree(current_node_tree1.right, current_node_tree2.left)

        return same_tree(root.left, root.right)


def test_isSymmetric():
    solution = Solution()
    assert solution.isSymmetric(TreeNode(1, TreeNode(2), TreeNode(3))) == False
    assert solution.isSymmetric(TreeNode(1, TreeNode(2), TreeNode(2))) == True
