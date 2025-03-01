<h1> Binary Trees </h1>

<h2> Table of Contents </h2>

- [Definition](#definition)
- [Visual Representation](#visual-representation)
- [Implementation](#implementation)
- [Basic Operations](#basic-operations)
- [Tree Traversal Methods](#tree-traversal-methods)
  - [Depth-First Search (DFS)](#depth-first-search-dfs)
    - [1. In-order Traversal (Left → Root → Right)](#1-in-order-traversal-left--root--right)
    - [2. Pre-order Traversal (Root → Left → Right)](#2-pre-order-traversal-root--left--right)
    - [3. Post-order Traversal (Left → Right → Root)](#3-post-order-traversal-left--right--root)
  - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
  - [Comparison of Traversal Methods](#comparison-of-traversal-methods)
- [Warmup Problems](#warmup-problems)
  - [Validate Binary Search Tree](#validate-binary-search-tree)
  - [Find Kth Smallest Element](#find-kth-smallest-element)
  - [Lowest Common Ancestor in BST](#lowest-common-ancestor-in-bst)

## Definition

A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.

A Binary Search Tree is a binary tree with the following properties:

- The left subtree of a node contains only nodes with values less than the node's value
- The right subtree of a node contains only nodes with values greater than the node's value
- Both the left and right subtrees must also be binary search trees
- Typically, duplicate values are not allowed.

## Visual Representation

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

## Implementation

```python
class TreeNode:
    def __init__(self, val=0):
        self.val = val      # Initialize the node's value
        self.left = None    # Initialize the left child as None
        self.right = None   # Initialize the right child as None

class BST:
    def __init__(self):
        self.root = None  # Initialize the root of the BST as None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)  # If the tree is empty, set the root to a new TreeNode
            return

        current = self.root
        while current:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)  # Insert the new node as the left child
                    return
                current = current.left  # Move to the left child
            else:
                if not current.right:
                    current.right = TreeNode(val)  # Insert the new node as the right child
                    return
                current = current.right  # Move to the right child

    def search(self, val):
        current = self.root
        while current:
            if val == current.val:
                return current  # Return the node if the value is found
            current = current.left if val < current.val else current.right  # Move to the left or right child
        return None  # Return None if the value is not found
```

## Basic Operations

| Operation | Average Case | Worst Case |
| --------- | ------------ | ---------- |
| Search    | $O(\log n)$  | $O(n)$     |
| Insert    | $O(\log n)$  | $O(n)$     |
| Delete    | $O(\log n)$  | $O(n)$     |

## Tree Traversal Methods

### Depth-First Search (DFS)

DFS explores as far as possible along each branch before backtracking. There are three main types of DFS traversals:

#### 1. In-order Traversal (Left → Root → Right)

Visits nodes in ascending order in a BST.

<details>
<summary>Recursive Implementation</summary>

```python
def inorder_recursive(root):
    def traverse(node, result):
        if not node:
            return
        traverse(node.left, result)   # Left
        result.append(node.val)       # Root
        traverse(node.right, result)  # Right

    result = []
    traverse(root, result)
    return result
```

</details>

<details>
<summary>Iterative Implementation</summary>

```python
def inorder_iterative(root):
    result = []
    stack = []
    current = root

    while stack or current:
        # Reach the leftmost node
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
```

</details>

#### 2. Pre-order Traversal (Root → Left → Right)

Useful for creating a copy of the tree or serializing tree structure.

<details>
<summary>Recursive Implementation</summary>

```python
def preorder_recursive(root):
    def traverse(node, result):
        if not node:
            return
        result.append(node.val)       # Root
        traverse(node.left, result)   # Left
        traverse(node.right, result)  # Right

    result = []
    traverse(root, result)
    return result
```

</details>

<details>
<summary>Iterative Implementation</summary>

```python
def preorder_iterative(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

</details>

#### 3. Post-order Traversal (Left → Right → Root)

Useful when deleting nodes or calculating directory sizes.

<details>
<summary>Recursive Implementation</summary>

```python
def postorder_recursive(root):
    def traverse(node, result):
        if not node:
            return
        traverse(node.left, result)   # Left
        traverse(node.right, result)  # Right
        result.append(node.val)       # Root

    result = []
    traverse(root, result)
    return result
```

</details>

<details>
<summary>Iterative Implementation</summary>

```python
def postorder_iterative(root):
    if not root:
        return []

    result = []
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()
        if visited:
            result.append(node.val)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return result
```

</details>

### Breadth-First Search (BFS)

Also known as level-order traversal, BFS visits all nodes at the current depth before moving to nodes at the next depth level.

<details>
<summary>Recursive Implementation</summary>

```python
def bfs_recursive(root):
    def get_level_nodes(node, level, result):
        if not node:
            return
        if len(result) == level:
            result.append([])

        result[level].append(node.val)
        get_level_nodes(node.left, level + 1, result)
        get_level_nodes(node.right, level + 1, result)

    result = []
    get_level_nodes(root, 0, result)
    return result
```

</details>

<details>
<summary>Iterative Implementation</summary>

```python
from collections import deque

def bfs_iterative(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

</details>

### Comparison of Traversal Methods

| Traversal Method | Use Case                      | Time Complexity | Space Complexity |
| ---------------- | ----------------------------- | --------------- | ---------------- |
| In-order         | Get sorted elements in BST    | $O(n)$          | $O(h)$           |
| Pre-order        | Copy/serialize tree structure | $O(n)$          | $O(h)$           |
| Post-order       | Delete nodes/calculate sizes  | $O(n)$          | $O(h)$           |
| BFS              | Level-by-level processing     | $O(n)$          | $O(w)$           |

Where:

- $n$ is the number of nodes
- $h$ is the height of the tree
- $w$ is the maximum width of the tree

<details>
<summary>Test Cases for All Traversals</summary>

```python
def test_traversals():
    # Create test BST:
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    # Test in-order
    assert inorder_recursive(root) == [1,2,3,4,5,6,7]
    assert inorder_iterative(root) == [1,2,3,4,5,6,7]

    # Test pre-order
    assert preorder_recursive(root) == [4,2,1,3,6,5,7]
    assert preorder_iterative(root) == [4,2,1,3,6,5,7]

    # Test post-order
    assert postorder_recursive(root) == [1,3,2,5,7,6,4]
    assert postorder_iterative(root) == [1,3,2,5,7,6,4]

    # Test BFS
    assert bfs_iterative(root) == [[4],[2,6],[1,3,5,7]]
    assert bfs_recursive(root) == [[4],[2,6],[1,3,5,7]]
```

</details>

## Warmup Problems

### Validate Binary Search Tree

Determine if a binary tree is a valid BST.

<details>
<summary>Solution</summary>

```python
def is_valid_bst(root):
    def validate(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root)
```

</details>

<details>
<summary>Test Cases</summary>

```python
def test_is_valid_bst():
    # Valid BST
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    assert is_valid_bst(root) == True

    # Invalid BST (violates left subtree property)
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.right = TreeNode(6)  # Invalid: 6 > 5
    assert is_valid_bst(root) == False

    # Single node
    root = TreeNode(1)
    assert is_valid_bst(root) == True

    # Empty tree
    assert is_valid_bst(None) == True
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$ where n is the number of nodes.
- Space complexity: $O(h)$ where h is the height of the tree.

</details>

### Find Kth Smallest Element

Find the kth smallest element in a BST.

<details>
<summary>Solution</summary>

```python
def kth_smallest(root, k):
    lst = []

    def k_smallest(node):
        if not node: return

        k_smallest(node.left)
        lst.append(node.val)
        k_smallest(node.right)

    k_smallest(root)
    return lst[k-1]
```

</details>

<details>
<summary>Test Cases</summary>

```python
def test_kth_smallest():
    # Create BST: 3,1,4,null,2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 2) == 2
    assert kth_smallest(root, 3) == 3
    assert kth_smallest(root, 4) == 4

    # Single node
    root = TreeNode(1)
    assert kth_smallest(root, 1) == 1
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$ where n is the number of nodes.
- Space complexity: $O(n)$ for the list.

</details>

### Lowest Common Ancestor in BST

Find the lowest common ancestor of two nodes in a BST.

<details>
<summary>Solution</summary>

```python
def lowest_common_ancestor(root, p, q):
    current = root

    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            return current
```

</details>

<details>
<summary>Test Cases</summary>

```python
def test_lca():
    # Create BST:     6
    #               /   \
    #              2     8
    #             / \   / \
    #            0   4 7   9
    #               / \
    #              3   5

    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    # Test case 1: LCA of 2 and 8 should be 6
    assert lowest_common_ancestor(root, root.left, root.right).val == 6

    # Test case 2: LCA of 2 and 4 should be 2
    assert lowest_common_ancestor(root, root.left, root.left.right).val == 2
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(h)$ where h is the height of the tree.
- Space complexity: $O(1)$ as it uses iterative approach.

</details>
