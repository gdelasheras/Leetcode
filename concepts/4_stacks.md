<h1> Stacks </h1>
<h2> Table of Contents </h2>

- [Definition](#definition)
- [Operations](#operations)
- [Visual Example](#visual-example)
- [Implementations](#implementations)
  - [Using a class with a list](#using-a-class-with-a-list)
  - [Just a list](#just-a-list)
- [Common Applications](#common-applications)
- [Warm up exercises](#warm-up-exercises)
  - [Example 1: Balanced parentheses](#example-1-balanced-parentheses)
  - [Example 2: Reverse a string](#example-2-reverse-a-string)
  - [Example 3: Evaluate Reverse Polish Notation](#example-3-evaluate-reverse-polish-notation)

## Definition

A `stack` is a data structure that follows the `Last In First Out (LIFO)` principle. This means the last element added to the `stack` is the first one to be removed. `Stacks` are used in many algorithms and are a fundamental data structure in computer science.

## Operations

A `stack` supports the following operations:

| Operation    | Time Complexity | Description                                                   |
| ------------ | :-------------: | ------------------------------------------------------------- |
| `push(item)` |     $O(1)$      | Adds an item to the top of the stack.                         |
| `pop()`      |     $O(1)$      | Removes and returns the item at the top of the stack.         |
| `peek()`     |     $O(1)$      | Returns the item at the top of the stack without removing it. |
| `is_empty()` |     $O(1)$      | Returns `True` if the stack is empty, `False` otherwise.      |
| `size()`     |     $O(1)$      | Returns the number of items in the stack.                     |
| `clear()`    |     $O(1)$      | Removes all items from the stack.                             |

## Visual Example

Consider a stack where we perform the following operations:

1. `push(1)`
2. `push(2)`
3. `push(3)`
4. `pop()`
5. `peek()`

Here's how the stack looks at each step:

```
Initial Stack:   After push(1):   After push(2):
|   |            | 1 |            | 2 |
|___|            |___|            | 1 |
                                  |___|

After push(3):   After pop():     After peek():
| 3 |            | 2 |            | 2 |
| 2 |            | 1 |            | 1 |
| 1 |            |___|            |___|
|___|
              3 is removed      Top element is 2
```

## Implementations

### Using a class with a list

A `stack` can be implemented using a `list`. The top of the `stack` is the last element of the `list`.

```python
class Stack:
    def __init__(self):
        self.items = []                # Initialize an empty list to store stack items

    def push(self, item):
        self.items.append(item)        # Add an item to the top of the stack

    def pop(self):
        if not self.is_empty():        # Check if the stack is not empty
            return self.items.pop()    # Remove and return the top item of the stack

    def peek(self):
        if not self.is_empty():        # Check if the stack is not empty
            return self.items[-1]      # Return the top item of the stack without removing it

    def is_empty(self):
        return len(self.items) == 0    # Return True if the stack is empty, False otherwise

    def size(self):
        return len(self.items)         # Return the number of items in the stack

    def clear(self):
        self.items = []                # Remove all items from the stack
```

### Just a list

Alternatively, a `stack` can be implemented using a `list`.

```python
stack = []

stack.append(1)  # push
stack.append(2)  # push
stack.pop()      # pop
stack[-1]        # peek
len(stack)       # size
stack.clear()    # clear
```

## Common Applications

- Undo/Redo Operations.
- Expression Evaluation.
- Backtracking Algorithms.
- Call Stack for Recursive Functions.
- Graph Traversal (DFS).
- Memory Management (Stack-based allocation).

## Warm up exercises

### Example 1: Balanced parentheses

Given a string containing only parentheses, determine if the parentheses are balanced. A string is balanced if every opening parenthesis has a corresponding closing parenthesis and the pairs of parentheses are properly nested.

<details>
<summary>Solution</summary>

```python
def is_balanced_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return len(stack) == 0
```

</details>

<details>
<summary>Test cases</summary>

```python
assert is_balanced_parentheses('()') == True
assert is_balanced_parentheses('()[]{}') == True
assert is_balanced_parentheses('(]') == False
assert is_balanced_parentheses('([)]') == False
assert is_balanced_parentheses('{[]}') == True
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$
- Space complexity: $O(n)$, where $n$ is the length of the string.
</details>

### Example 2: Reverse a string

Reverse a string using a `stack`.

<details>
<summary>Solution</summary>

```python
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_s = ''
    while stack:
        reversed_s += stack.pop()
    return reversed_s
```

</details>

<details>
<summary>Test cases</summary>

```python
assert reverse_string('hello') == 'olleh'
assert reverse_string('world') == 'dlrow'
assert reverse_string('') == ''
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$
- Space complexity: $O(n)$, where $n$ is the length of the string.
</details>

### Example 3: Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

<details>
<summary>Solution</summary>

```python
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack.pop()
```

</details>

<details>
<summary>Test cases</summary>

```python
assert eval_rpn(['2', '1', '+', '3', '*']) == 9
assert eval_rpn(['4', '13', '5', '/', '+']) == 6
assert eval_rpn(['10', '6', '9', '3', '/', '-', '*']) == 90
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$
- Space complexity: $O(n)$, where $n$ is the number of tokens.
</details>
