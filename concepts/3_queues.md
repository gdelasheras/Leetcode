<h1> Queues </h1>
<h2> Table of Contents </h2>

- [Definition](#definition)
- [Visual Representation](#visual-representation)
- [Operations](#operations)
- [Implementations](#implementations)
  - [Using a class](#using-a-class)
    - [Time Complexity](#time-complexity)
  - [Deque](#deque)
    - [Time Complexity](#time-complexity-1)
- [Warm up exercises](#warm-up-exercises)
  - [Example 1: Students and Lunch](#example-1-students-and-lunch)

## Definition

A `queue` is a data structure that follows the `First In First Out (FIFO)` principle. This means that the first element added to the queue is the first one to be removed.

## Visual Representation

```

<---------------------------------------

+-----+    +-----+    +-----+    +-----+
|  1  | -- |  2  | -- |  3  | -- |  4  |
+-----+    +-----+    +-----+    +-----+
 Front                             Rear
```

In this representation, the `Front` is where elements are removed from the queue, and the `Rear` is where elements are added.

## Operations

A queue supports the following operations:

| Operation       | Description                                                     |
| --------------- | --------------------------------------------------------------- |
| `enqueue(item)` | Adds an item to the end of the queue.                           |
| `dequeue()`     | Removes and returns the item at the front of the queue.         |
| `first()`       | Returns the item at the front of the queue without removing it. |
| `is_empty()`    | Returns `True` if the queue is empty, `False` otherwise.        |
| `size()`        | Returns the number of items in the queue.                       |
| `clear()`       | Removes all items from the queue.                               |
| `last()`        | Returns the item at the end of the queue without removing it.   |

## Implementations

### Using a class

A queue can be implemented using a list. The front of the queue is the first element of the list.

```python
class Queue:
    def __init__(self):
        self.items = []                 # Initialize an empty list to store queue items

    def enqueue(self, item):
        self.items.append(item)         # Add an item to the end of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)    # Remove and return the item at the front of the queue

    def first(self):
        if not self.is_empty():
            return self.items[0]        # Return the item at the front of the queue without removing it

    def is_empty(self):
        return len(self.items) == 0     # Check if the queue is empty

    def size(self):
        return len(self.items)          # Return the number of items in the queue

    def clear(self):
        self.items = []                 # Remove all items from the queue
```

#### Time Complexity

The time complexity of the operations on a queue implemented using a list is as follows:

| Operation       | Time Complexity | Explanation                                                                  |
| --------------- | :-------------: | ---------------------------------------------------------------------------- |
| `enqueue(item)` |     $O(1)$      | Adding an item to the end of the list takes constant time.                   |
| `dequeue()`     |     $O(n)$      | Removing the first item requires shifting all other items one position left. |
| `first()`       |     $O(1)$      | Accessing the first item is a constant time operation.                       |
| `is_empty()`    |     $O(1)$      | Checking if the list is empty takes constant time.                           |
| `size()`        |     $O(1)$      | Getting the length of the list is a constant time operation.                 |
| `clear()`       |     $O(1)$      | Clearing the list is a constant time operation.                              |
| `last()`        |     $O(1)$      | Accessing the last item is a constant time operation.                        |

### Deque

Alternatively, a queue can be implemented using a `deque`, which is a double-ended queue.

```python
from collections import deque

queue = deque()

queue.append(1)  # enqueue 1
queue.append(2)  # enqueue 2
queue.popleft()  # dequeue 1
queue[0]         # first 2
len(queue)       # size 1
queue.clear()    # clear
queue[-1]        # last 2
```

#### Time Complexity

The time complexity of the operations on a queue implemented using a `deque` is as follows:

| Operation      | Time Complexity | Explanation                                                   |
| -------------- | :-------------: | ------------------------------------------------------------- |
| `append(item)` |     $O(1)$      | Adding an item to the end of the deque takes constant time.   |
| `pop_left()`   |     $O(1)$      | Removing the first item from the deque takes constant time.   |
| `deque[0]`     |     $O(1)$      | Accessing the first item is a constant time operation.        |
| `len(deque)`   |     $O(1)$      | Getting the length of the deque is a constant time operation. |
| `clear()`      |     $O(1)$      | Clearing the deque is a constant time operation.              |
| `deque[-1]`    |     $O(1)$      | Accessing the last item is a constant time operation.         |

## Warm up exercises

### Example 1: Students and Lunch

You are given two arrays: `students` and `sandwiches`. Each element in the `students` array represents a student's preference (0 for a circular sandwich, 1 for a square sandwich). Each element in the `sandwiches` array represents the type of sandwich available in the stack (0 for circular, 1 for square). The sandwiches are stacked such that the first element is on the top of the stack.

Students are in a queue, and they will take the sandwich on the top of the stack if it matches their preference. If not, they will move to the end of the queue. This process continues until no student wants the sandwich on the top of the stack.

Return the number of students that are unable to eat.

<details>
<summary>Solution</summary>

```python
from collections import deque

def count_students(students, sandwiches):
    if len(students) != len(sandwiches):
        raise ValueError("The number of students and sandwiches must be equal.")

    student_queue = deque(students)
    sandwich_stack = sandwiches
    count = 0

    while student_queue and count < len(student_queue):
        if student_queue[0] == sandwich_stack[0]:
            student_queue.popleft()
            sandwich_stack.pop(0)
            count = 0  # Reset count since a sandwich was taken
        else:
            student_queue.append(student_queue.popleft())
            count += 1  # Increment count since no sandwich was taken

    return len(student_queue)
```

</details>

<details>
<summary>Test Cases</summary>

```python
def test_count_students():
    assert count_students([1, 1, 0, 0], [0, 1, 0, 1]) == 0
    assert count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3
    assert count_students([0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 1, 1]) == 0

    try:
        count_students([1, 0], [0, 1, 0])
    except ValueError as e:
        assert str(e) == "The number of students and sandwiches must be equal."

test_count_students()
```

</details>

<details>
<summary>Complexities</summary>

- **Time Complexity**: $O(m \times n)$, where $m = \min(\text{len(students)}, \text{len(sandwiches)})$ and $n$ is the number of students. This accounts for the potential repeated cycling through the queue.
- **Space Complexity**: $O(n)$, where $n$ is the length of the `students` array, due to the use of a deque to manage the student queue.

</details>
