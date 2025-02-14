<h1> Doubly Linked Lists </h1>
<h2> Table of Contents </h2>

- [Definition](#definition)
- [Types of Linked Lists](#types-of-linked-lists)
- [Doubly Linked Lists](#doubly-linked-lists)
  - [Visual Representation](#visual-representation)
- [Operations](#operations)
- [Implementation](#implementation)
- [Time Complexity](#time-complexity)
- [Example Problems](#example-problems)
  - [Palindrome Check](#palindrome-check)
  - [Reverse a doubly linked list.](#reverse-a-doubly-linked-list)
  - [Remove Duplicates](#remove-duplicates)

## Definition

A linked list is a linear data structure where each element is a separate object, called a node. Each node contains two items: the data and a reference (or link) to the next node in the sequence. This structure allows for efficient insertion and removal of elements from any position in the sequence.

## Types of Linked Lists

1. **Singly Linked List**: Each node contains a single link to the next node.
2. **Doubly Linked List**: Each node contains two links, one to the next node and one to the previous node.

## Doubly Linked Lists

A `doubly linked list` is a data structure where each node contains data and two references (or pointers): one to the next node and one to the previous node in the sequence. This bidirectional linking allows for more flexible operations compared to singly linked lists.

### Visual Representation

```
+------+------+      +------+------+    +------+------+    +------+------+
|  A   | next |  ->  |  B   | next | -> |  C   | next | -> |  D   | None |
+------+------+      +------+------+    +------+------+    +------+------+
| None | ---- |  <-  | prev | ---- | <- | prev | ---- | <- | prev | ---- |
+------+------+      +------+------+    +------+------+    +------+------+
```

## Operations

A doubly linked list supports the following operations:

| Operation           | Description                                             |
| ------------------- | ------------------------------------------------------- |
| `append(item)`      | Adds an item to the end of the list.                    |
| `prepend(item)`     | Adds an item to the beginning of the list.              |
| `delete(item)`      | Removes the first occurrence of the item from the list. |
| `insert(pos, item)` | Inserts an item at the specified position.              |
| `get(pos)`          | Returns the item at the specified position.             |
| `is_empty()`        | Returns `True` if the list is empty, `False` otherwise. |
| `size()`            | Returns the number of items in the list.                |
| `clear()`           | Removes all items from the list.                        |

## Implementation

```python
class Node:
    def __init__(self, data):
        # Initialize a node with data, and pointers to the next and previous nodes
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list with head, tail, and size
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        # Add a new node with the given data to the end of the list
        new_node = Node(data)
        if not self.head:
            # If the list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, link the new node to the current tail and update the tail
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, data):
        # Add a new node with the given data to the beginning of the list
        new_node = Node(data)
        if not self.head:
            # If the list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, link the new node to the current head and update the head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def delete(self, data):
        # Remove the first occurrence of a node with the given data
        current = self.head
        while current:
            if current.data == data:
                # If the node to delete is found, update the links of neighboring nodes
                if current.prev:
                    current.prev.next = current.next
                else:
                    # If deleting the head, update the head
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    # If deleting the tail, update the tail
                    self.tail = current.prev

                self._size -= 1
                return
            current = current.next

    def insert(self, pos, data):
        # Insert a new node with the given data at the specified position
        if pos < 0 or pos > self._size:
            raise IndexError("Position out of range")

        if pos == 0:
            # If inserting at the head, use prepend
            self.prepend(data)
            return

        if pos == self._size:
            # If inserting at the tail, use append
            self.append(data)
            return

        # Otherwise, find the position and insert the new node
        new_node = Node(data)
        current = self.head
        for _ in range(pos):
            current = current.next

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self._size += 1

    def get(self, pos):
        # Retrieve the data of the node at the specified position
        if pos < 0 or pos >= self._size:
            raise IndexError("Position out of range")

        if pos <= self._size // 2:
            # If the position is in the first half, traverse from the head
            current = self.head
            for _ in range(pos):
                current = current.next
        else:
            # If the position is in the second half, traverse from the tail
            current = self.tail
            for _ in range(self._size - 1 - pos):
                current = current.prev
        return current.data

    def is_empty(self):
        # Check if the list is empty
        return self.head is None

    def size(self):
        # Return the number of nodes in the list
        return self._size

    def clear(self):
        # Remove all nodes from the list
        self.head = None
        self.tail = None
        self._size = 0
```

## Time Complexity

| Operation           | Time Complexity      | Explanation                                    |
| ------------------- | -------------------- | ---------------------------------------------- |
| `append(item)`      | $O(1)$               | Direct access to tail node                     |
| `prepend(item)`     | $O(1)$               | Direct access to head node                     |
| `delete(item)`      | $O(n)$               | May need to traverse the list to find the item |
| `insert(pos, item)` | $O(min(pos, n-pos))$ | Can traverse from either end                   |
| `get(pos)`          | $O(min(pos, n-pos))$ | Can traverse from either end                   |
| `is_empty()`        | $O(1)$               | Only needs to check if head is None            |
| `size()`            | $O(1)$               | Maintains a size counter                       |
| `clear()`           | $O(1)$               | Only needs to set head and tail to None        |

## Example Problems

### Palindrome Check

Check if a doubly linked list is a palindrome.

<details>
<summary>Solution</summary>

```python
def is_palindrome(dll):
    if dll.is_empty() or dll.size() == 1:
        return True

    left = dll.head
    right = dll.tail

    for _ in range(dll.size() // 2):
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev

    return True
```

</details>

<details>
<summary>Test cases</summary>

```python
assert is_palindrome([1, 2, 3, 2, 1]) == True
assert is_palindrome([1, 2, 3, 3, 2, 1]) == True
assert is_palindrome([1, 2, 3, 4, 5]) == False
assert is_palindrome([]) == True
assert is_palindrome([1]) == True
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$, where $n$ is the size of the linked list.
- Space complexity: $O(1)$.

</details>

### Reverse a doubly linked list.

<details>
<summary>Solution</summary>

```python
def reverse_list(dll):
    if dll.is_empty() or dll.size() == 1:
        return

    current = dll.head
    while current:
        # Swap next and prev pointers
        temp = current.next
        current.next = current.prev
        current.prev = temp
        current = temp

    # Swap head and tail
    temp = dll.head
    dll.head = dll.tail
    dll.tail = temp
```

</details>

<details>
<summary>Test cases</summary>

```python
assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert reverse_list([]) == []
assert reverse_list([1]) == [1]
assert reverse_list([1] * 100000) == [1] * 100000
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$, where $n$ is the size of the linked list.
- Space complexity: $O(1)$.

</details>

### Remove Duplicates

Remove duplicate elements from a sorted doubly linked list.

<details>
<summary>Solution</summary>

```python
def remove_duplicates(dll):
    if dll.is_empty() or dll.size() == 1:
        return

    current = dll.head
    while current and current.next:
        if current.data == current.next.data:
            # Skip the duplicate node
            current.next = current.next.next
            if current.next:
                current.next.prev = current
            dll._size -= 1
        else:
            current = current.next

    # Update tail if needed
    current = dll.head
    while current and current.next:
        current = current.next
    dll.tail = current
```

</details>

<details>
<summary>Test cases</summary>

```python
assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([1]) == [1]
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$, where $n$ is the size of the linked list.
- Space complexity: $O(1)$.

</details>
