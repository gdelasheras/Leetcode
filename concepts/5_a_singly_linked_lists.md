<h1> Linked Lists </h1>
<h2> Table of Contents </h2>

- [Definition](#definition)
- [Types of Linked Lists](#types-of-linked-lists)
- [Singly Linked List](#singly-linked-list)
  - [Visual Representation](#visual-representation)
  - [Operations](#operations)
  - [Implementation](#implementation)
  - [Time Complexity](#time-complexity)
- [Warmup Problems](#warmup-problems)
  - [Reverse a Linked List](#reverse-a-linked-list)
  - [Detect Cycle](#detect-cycle)
  - [Find Middle Node](#find-middle-node)

## Definition

A linked list is a linear data structure where each element is a separate object, called a node. Each node contains two items: the data and a reference (or link) to the next node in the sequence. This structure allows for efficient insertion and removal of elements from any position in the sequence.

## Types of Linked Lists

1. **Singly Linked List**: Each node contains a single link to the next node.
2. **Doubly Linked List**: Each node contains two links, one to the next node and one to the previous node.

## Singly Linked List

A `singly linked list` is a data structure consisting of nodes where each node contains data and a reference (or pointer) to the next node in the sequence. The last node points to `None`, indicating the end of the list.

### Visual Representation

```
+-----+------+    +-----+------+    +-----+------+    +-----+------+
|  A  | next | -> |  B  | next | -> |  C  | next | -> |  D  | None |
+-----+------+    +-----+------+    +-----+------+    +-----+------+
```

### Operations

A singly linked list supports the following operations:

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

### Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data      # Store the data
        self.next = None      # Initialize the next pointer to None

class SinglyLinkedList:
    def __init__(self):
        self.head = None      # Initialize the head of the list
        self._size = 0        # Initialize the size of the list

    def append(self, data):
        new_node = Node(data) # Create a new node with the given data
        if not self.head:     # If the list is empty
            self.head = new_node # Set the new node as the head
        else:
            current = self.head
            while current.next: # Traverse to the end of the list
                current = current.next
            current.next = new_node # Link the last node to the new node
        self._size += 1       # Increment the size of the list

    def prepend(self, data):
        new_node = Node(data) # Create a new node with the given data
        new_node.next = self.head # Link the new node to the current head
        self.head = new_node  # Update the head to the new node
        self._size += 1       # Increment the size of the list

    def delete(self, data):
        if not self.head:     # If the list is empty, do nothing
            return

        if self.head.data == data: # If the head is the node to delete
            self.head = self.head.next # Update the head to the next node
            self._size -= 1     # Decrement the size of the list
            return

        current = self.head
        while current.next and current.next.data != data: # Traverse to find the node
            current = current.next

        if current.next:       # If the node is found
            current.next = current.next.next # Bypass the node to delete it
            self._size -= 1    # Decrement the size of the list

    def insert(self, pos, data):
        if pos < 0 or pos > self._size: # Check for valid position
            raise IndexError("Position out of range")

        if pos == 0:           # If inserting at the head
            self.prepend(data)
            return

        new_node = Node(data)  # Create a new node
        current = self.head
        for _ in range(pos - 1): # Traverse to the position
            current = current.next
        new_node.next = current.next # Link the new node to the next node
        current.next = new_node # Link the previous node to the new node
        self._size += 1        # Increment the size of the list

    def get(self, pos):
        if pos < 0 or pos >= self._size: # Check for valid position
            raise IndexError("Position out of range")

        current = self.head
        for _ in range(pos):   # Traverse to the position
            current = current.next
        return current.data    # Return the data at the position

    def is_empty(self):
        return self.head is None # Return True if the list is empty

    def size(self):
        return self._size      # Return the size of the list

    def clear(self):
        self.head = None       # Clear the list by setting head to None
        self._size = 0         # Reset the size to 0
```

### Time Complexity

| Operation           | Time Complexity | Explanation                                           |
| ------------------- | :-------------: | ----------------------------------------------------- |
| `append(item)`      |     $O(n)$      | Must traverse to the end of the list                  |
| `prepend(item)`     |     $O(1)$      | Only needs to update the head pointer                 |
| `delete(item)`      |     $O(n)$      | May need to traverse the entire list to find the item |
| `insert(pos, item)` |     $O(n)$      | May need to traverse to the position                  |
| `get(pos)`          |     $O(n)$      | Must traverse to the specified position               |
| `is_empty()`        |     $O(1)$      | Only needs to check if head is None                   |
| `size()`            |     $O(1)$      | Maintains a size counter                              |
| `clear()`           |     $O(1)$      | Only needs to set head to None                        |

## Warmup Problems

### Reverse a Linked List

Write a function to reverse a singly linked list.

<details>
<summary>Solution</summary>

```python
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev
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

### Detect Cycle

Determine if a singly linked list has a cycle.

<details>
<summary>Solution</summary>

```python
def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True
```

</details>

<details>
<summary>Test cases</summary>

```python
assert has_cycle([1, 2, 3, 4, 5]) == False
assert has_cycle([1, 2, 3, 4, 5, 1]) == True
assert has_cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$, where $n$ is the size of the linked list.
- Space complexity: $O(1)$.

</details>

### Find Middle Node

Find the middle node of a linked list.

<details>
<summary>Solution</summary>

```python
def find_middle(head):
    if not head:
        return None

    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

</details>

<details>
<summary>Test cases</summary>

```python
assert find_middle([1, 2, 3, 4, 5]) == 3
assert find_middle([1, 2, 3, 4, 5, 6]) == 4
assert find_middle([1, 2, 3, 4, 5, 6, 7]) == 4
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$, where $n$ is the size of the linked list.
- Space complexity: $O(1)$.

</details>
