<h1> Heaps </h1>
<h2> Table of Contents </h2>

- [Definition](#definition)
- [Visual Representation](#visual-representation)
  - [Min Heap](#min-heap)
  - [Max Heap](#max-heap)
- [Operations](#operations)
- [Implementation](#implementation)
  - [Min Heap Using heapq](#min-heap-using-heapq)
  - [Max Heap Using heapq](#max-heap-using-heapq)
- [Common Applications](#common-applications)
- [Warmup Problems](#warmup-problems)
  - [Find K Largest Elements](#find-k-largest-elements)
  - [Merge K Sorted Lists](#merge-k-sorted-lists)
  - [Running Median](#running-median)

## Definition

A heap is a specialized tree-based data structure that satisfies the heap property:

- In a max heap, for any given node C, if P is a parent node of C, then the value of P is greater than or equal to the value of C
- In a min heap, for any given node C, if P is a parent node of C, then the value of P is less than or equal to the value of C

Python's `heapq` module implements a min heap.

## Visual Representation

### Min Heap

```
       1          Level 0
     /   \
    3     2       Level 1
   / \   /
  6   4 5         Level 2
```

Consider the following operations:

```
1. **Push 5:**          2. **Push 3:**          3. **Push 8:**

       5                     3                     3
                            / \                   / \
                           5                     5   8

   (3 is smaller than 5, so it becomes the root)

2. **Pop (remove 3):**  5. **Push 2:**          6. **Push 7:**

       5                     2                     2
      /                     / \                   / \
     8                     5   8                 5   8
                                                 /
                                                7

   (5 replaces 3, and the heap is restructured)
   (2 is smaller than 5, so it becomes the root)

3. **Pop (remove 2):**  8. **Push 1:**          9. **Pop (remove 1):**

       5                     1                     5
      / \                   / \                   / \
     7   8                 5   8                 7   8
                          /
                         7

   (5 replaces 2, and the heap is restructured)
   (1 is smaller than 5, so it becomes the root)
   (5 replaces 1, and the heap is restructured)
```

### Max Heap

```
       5          Level 0
     /   \
    3     2       Level 1
   / \   /
  6   4 5         Level 2
```

## Operations

| Operation       | Time Complexity | Description                                          |
| --------------- | :-------------: | ---------------------------------------------------- |
| `heappush()`    |   $O(\log n)$   | Add an element to the heap                           |
| `heappop()`     |   $O(\log n)$   | Remove and return the smallest element               |
| `heapify()`     |     $O(n)$      | Transform a list into a heap in-place                |
| `heappushpop()` |   $O(\log n)$   | Push item on heap, then pop and return smallest item |
| `heapreplace()` |   $O(\log n)$   | Pop and return smallest item, then push new item     |
| `nlargest()`    |  $O(n \log k)$  | Return the k largest elements                        |
| `nsmallest()`   |  $O(n \log k)$  | Return the k smallest elements                       |

## Implementation

### Min Heap Using heapq

```python
from heapq import heappush, heappop, heapify

class MinHeap:
    def __init__(self):                      # Initialize an empty heap
        self.heap = heapify([])

    def push(self, val):                     # Push a value onto the heap
        heappush(self.heap, val)

    def pop(self):                           # Pop the smallest value from the heap
        if not self.is_empty():              # Check if the heap is not empty
            return heappop(self.heap)

    def peek(self):                          # Peek at the smallest value without popping it
        if not self.is_empty():              # Check if the heap is not empty
            return self.heap[0]

    def is_empty(self):                      # Check if the heap is empty
        return len(self.heap) == 0

    def size(self):                          # Return the size of the heap
        return len(self.heap)
```

### Max Heap Using heapq

Since `heapq` only provides min heap, we can implement max heap by negating the values:

```python
from heapq import heappush, heappop, heapify

class MaxHeap:
    def __init__(self):                      # Initialize an empty heap
        self.heap = heapify([])

    def push(self, val):                     # Push a value onto the heap (negated)
        heappush(self.heap, -val)

    def pop(self):                           # Pop the largest value from the heap
        if not self.is_empty():              # Check if the heap is not empty
            return -heappop(self.heap)

    def peek(self):                          # Peek at the largest value without popping it
        if not self.is_empty():              # Check if the heap is not empty
            return -self.heap[0]

    def is_empty(self):                      # Check if the heap is empty
        return len(self.heap) == 0

    def size(self):                          # Return the size of the heap
        return len(self.heap)
```

## Common Applications

1. Priority Queues
2. Scheduling algorithms
3. Graph algorithms (Dijkstra's shortest path)
4. K-way merging
5. Finding kth largest/smallest elements
6. Median maintenance

## Warmup Problems

### Find K Largest Elements

<details>
<summary>Solution</summary>

```python
from heapq import nlargest

def find_k_largest(nums, k):
    return nlargest(k, nums)

# Alternative implementation using min heap
def find_k_largest_heap(nums, k):
    heap = []
    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)
    return sorted(heap, reverse=True)
```

</details>

<details>
<summary>Test Cases</summary>

```python
def test_k_largest():
    # Test case 1: Basic case
    assert find_k_largest([3,1,4,1,5,9,2,6,5], 3) == [9,6,5]

    # Test case 2: K equals array length
    assert find_k_largest([1,2,3,4,5], 5) == [5,4,3,2,1]

    # Test case 3: K equals 1
    assert find_k_largest([1,2,3,4,5], 1) == [5]

    # Test case 4: Array with duplicates
    assert find_k_largest([5,5,5,5], 2) == [5,5]
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n \log k)$
- Space complexity: $O(k)$
</details>

### Merge K Sorted Lists

<details>
<summary>Solution</summary>

```python
from heapq import heappush, heappop

def merge_k_sorted_lists(lists):
    heap = []
    result = []

    # Add first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heappop(heap)
        result.append(val)

        # If there are more elements in this list, add the next one
        if elem_idx + 1 < len(lists[list_idx]):
            next_elem = lists[list_idx][elem_idx + 1]
            heappush(heap, (next_elem, list_idx, elem_idx + 1))

    return result
```

</details>

<details>
<summary>Test Cases</summary>

```python
def test_merge_k_sorted():
    # Test case 1: Basic case
    lists = [[1,4,5],[1,3,4],[2,6]]
    assert merge_k_sorted_lists(lists) == [1,1,2,3,4,4,5,6]

    # Test case 2: Empty lists
    assert merge_k_sorted_lists([]) == []

    # Test case 3: Single list
    assert merge_k_sorted_lists([[1,2,3]]) == [1,2,3]

    # Test case 4: Lists with duplicates
    lists = [[1,1,1],[1,1,1]]
    assert merge_k_sorted_lists(lists) == [1,1,1,1,1,1]
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(N \log k)$ where N is total number of elements and k is number of lists.
- Space complexity: $O(k)$ for the heap.
</details>

### Running Median

<details>
<summary>Solution</summary>

```python
from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.small = []  # max heap for smaller half
        self.large = []  # min heap for larger half

    def addNum(self, num):
        # Push to appropriate heap
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        return float(self.large[0])
```

</details>

<details>
<summary>Test Cases</summary>

```python
def test_median_finder():
    mf = MedianFinder()

    # Test case 1: Single number
    mf.addNum(1)
    assert mf.findMedian() == 1.0

    # Test case 2: Even number of elements
    mf.addNum(2)
    assert mf.findMedian() == 1.5

    # Test case 3: Odd number of elements
    mf.addNum(3)
    assert mf.findMedian() == 2.0

    # Test case 4: Multiple elements
    mf = MedianFinder()
    nums = [6,10,2,6,5,0,6,3,1,0,0]
    for num in nums:
        mf.addNum(num)
    assert mf.findMedian() == 3.0
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity:
  - addNum: $O(\log n)$
  - findMedian: $O(1)$
- Space complexity: $O(n)$

</details>
