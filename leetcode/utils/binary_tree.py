from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_bst(values: List[int]) -> TreeNode:
    if not values:
        return None

    mid = len(values) // 2
    root = TreeNode(values[mid])

    root.left = list_to_bst(values[:mid])
    root.right = list_to_bst(values[mid+1:])

    return root


def bst_to_list_recursive(root: TreeNode) -> List[int]:
    def in_order_traversal(node: TreeNode) -> List[int]:
        if not node:
            return []

        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

    return in_order_traversal(root)
