<h1> Stack Exercises </h1>

<h2> Table of Contents </h2>

- [Exercise 1: Valid Parentheses](#exercise-1-valid-parentheses)
- [Exercise 2: Min Stack](#exercise-2-min-stack)
- [Exercise 3: Evaluate Reverse Polish Notation](#exercise-3-evaluate-reverse-polish-notation)
- [Exercise 4: Daily Temperatures](#exercise-4-daily-temperatures)
- [Exercise 5: Next Greater Element I](#exercise-5-next-greater-element-i)
- [Exercise 6: Simplify Path](#exercise-6-simplify-path)
- [Exercise 7: Decode String](#exercise-7-decode-string)
- [Exercise 8: Basic Calculator II](#exercise-8-basic-calculator-ii)
- [Exercise 9: Largest Rectangle in Histogram](#exercise-9-largest-rectangle-in-histogram)
- [Exercise 10: Asteroid Collision](#exercise-10-asteroid-collision)

## Exercise 1: Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

```python
def is_valid_parentheses(s: str) -> bool:
    """
    :param s: input string containing parentheses
    :return: true if the string is valid, false otherwise
    """
    pass
```

<h3> Examples </h3>

```shell
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```

<details>
<summary>Tests</summary>

```python
def test_is_valid_parentheses():
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("(]") == False
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_is_valid_parentheses_edge_cases():
    assert is_valid_parentheses("") == True
    assert is_valid_parentheses("([{}])") == True
    assert is_valid_parentheses("([)]") == False
    assert is_valid_parentheses("{[]}") == True
```

</details>

<details>
<summary>Solution Code</summary>

```python
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the length of the string
- **Space Complexity**: $O(n)$, for the stack

</details>

## Exercise 2: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

```python
class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def get_min(self) -> int:
        pass
```

<h3> Examples </h3>

```shell
Input:
["MinStack","push","push","push","get_min","pop","top","get_min"]
[[],[-2],[0],[-3],[],[],[],[]]
Output:
[null,null,null,null,-3,null,0,-2]
```

<details>
<summary>Tests</summary>

```python
def test_min_stack():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.get_min() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.get_min() == -2
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_min_stack_edge_cases():
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(2)
    min_stack.push(-1)
    assert min_stack.get_min() == -1
    min_stack.pop()
    assert min_stack.get_min() == 1
    min_stack.pop()
    assert min_stack.get_min() == 1
```

</details>

<details>
<summary>Solution Code</summary>

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack.pop() == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def get_min(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(1)$ for all operations
- **Space Complexity**: $O(n)$, where $n$ is the number of elements in the stack

</details>

## Exercise 3: Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

```python
def eval_rpn(tokens: List[str]) -> int:
    """
    :param tokens: list of tokens in reverse polish notation
    :return: result of the expression
    """
    pass
```

<h3> Examples </h3>

```shell
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

<details>
<summary>Tests</summary>

```python
def test_eval_rpn():
    assert eval_rpn(["2","1","+","3","*"]) == 9
    assert eval_rpn(["4","13","5","/","+"]) == 6
    assert eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_eval_rpn_edge_cases():
    assert eval_rpn(["3","-4","+"]) == -1
    assert eval_rpn(["2","3","*","5","4","*","+"]) == 26
    assert eval_rpn(["5","1","2","+","4","*","+","3","-"]) == 14
```

</details>

<details>
<summary>Solution Code</summary>

```python
def eval_rpn(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token in "+-*/":
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Truncate towards zero
        else:
            stack.append(int(token))
    return stack[0]
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the number of tokens
- **Space Complexity**: $O(n)$, for the stack

</details>

## Exercise 4: Daily Temperatures

Given a list of daily temperatures `T`, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.

```python
def daily_temperatures(T: List[int]) -> List[int]:
    """
    :param T: list of daily temperatures
    :return: list of days to wait for a warmer temperature
    """
    pass
```

<h3> Examples </h3>

```shell
Input: T = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

<details>
<summary>Tests</summary>

```python
def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_daily_temperatures_edge_cases():
    assert daily_temperatures([90, 80, 70, 60]) == [0, 0, 0, 0]
    assert daily_temperatures([60, 70, 60, 70, 60, 70]) == [1, 0, 1, 0, 1, 0]
    assert daily_temperatures([70, 70, 70, 70]) == [0, 0, 0, 0]
```

</details>

<details>
<summary>Solution Code</summary>

```python
def daily_temperatures(T: List[int]) -> List[int]:
    result = [0] * len(T)
    stack = []
    for i, temp in enumerate(T):
        while stack and T[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the number of temperatures
- **Space Complexity**: $O(n)$, for the stack

</details>

## Exercise 5: Next Greater Element I

You are given two arrays (without duplicates) `nums1` and `nums2` where `nums1` is a subset of `nums2`. Find all the next greater numbers for `nums1`'s elements in the corresponding places of `nums2`.

```python
def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    :param nums1: subset of nums2
    :param nums2: list of numbers
    :return: list of next greater elements for nums1 in nums2
    """
    pass
```

<h3> Examples </h3>

```shell
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

<details>
<summary>Tests</summary>

```python
def test_next_greater_element():
    assert next_greater_element([4,1,2], [1,3,4,2]) == [-1,3,-1]
    assert next_greater_element([2,4], [1,2,3,4]) == [3,-1]
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_next_greater_element_edge_cases():
    assert next_greater_element([1], [1,2,3,4]) == [2]
    assert next_greater_element([4], [1,2,3,4]) == [-1]
    assert next_greater_element([], [1,2,3,4]) == []
```

</details>

<details>
<summary>Solution Code</summary>

```python
def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    next_greater = {}
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    return [next_greater.get(num, -1) for num in nums1]
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n + m)$, where $n$ is the length of `nums1` and $m$ is the length of `nums2`
- **Space Complexity**: $O(m)$, for the stack and hash map

</details>

## Exercise 6: Simplify Path

Given a string `path`, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

```python
def simplify_path(path: str) -> str:
    """
    :param path: input path string
    :return: simplified canonical path
    """
    pass
```

<h3> Examples </h3>

```shell
Input: path = "/home/"
Output: "/home"

Input: path = "/../"
Output: "/"

Input: path = "/home//foo/"
Output: "/home/foo"
```

<details>
<summary>Tests</summary>

```python
def test_simplify_path():
    assert simplify_path("/home/") == "/home"
    assert simplify_path("/../") == "/"
    assert simplify_path("/home//foo/") == "/home/foo"
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_simplify_path_edge_cases():
    assert simplify_path("/a/./b/../../c/") == "/c"
    assert simplify_path("/a/../../b/../c//.//") == "/c"
    assert simplify_path("/a//b////c/d//././/..") == "/a/b/c"
```

</details>

<details>
<summary>Solution Code</summary>

```python
def simplify_path(path: str) -> str:
    stack = []
    components = path.split('/')
    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)
    return '/' + '/'.join(stack)
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the length of the path
- **Space Complexity**: $O(n)$, for the stack

</details>

## Exercise 7: Decode String

Given an encoded string, return its decoded string.

```python
def decode_string(s: str) -> str:
    """
    :param s: encoded string
    :return: decoded string
    """
    pass
```

<h3> Examples </h3>

```shell
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"
```

<details>
<summary>Tests</summary>

```python
def test_decode_string():
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_decode_string_edge_cases():
    assert decode_string("10[a]") == "aaaaaaaaaa"
    assert decode_string("2[3[b]a]") == "bbabbba"
    assert decode_string("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
```

</details>

<details>
<summary>Solution Code</summary>

```python
def decode_string(s: str) -> str:
    stack = []
    current_num = 0
    current_string = ''
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string, current_num = '', 0
        elif char == ']':
            last_string, num = stack.pop()
            current_string = last_string + num * current_string
        else:
            current_string += char
    return current_string
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the length of the string
- **Space Complexity**: $O(n)$, for the stack

</details>

## Exercise 8: Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

```python
def calculate(s: str) -> int:
    """
    :param s: input expression string
    :return: result of the expression
    """
    pass
```

<h3> Examples </h3>

```shell
Input: s = "3+2*2"
Output: 7

Input: s = " 3/2 "
Output: 1

Input: s = " 3+5 / 2 "
Output: 5
```

<details>
<summary>Tests</summary>

```python
def test_calculate():
    assert calculate("3+2*2") == 7
    assert calculate(" 3/2 ") == 1
    assert calculate(" 3+5 / 2 ") == 5
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_calculate_edge_cases():
    assert calculate("14-3/2") == 13
    assert calculate("0") == 0
    assert calculate("1-1+1") == 1
```

</details>

<details>
<summary>Solution Code</summary>

```python
def calculate(s: str) -> int:
    if not s:
        return 0
    stack = []
    current_num = 0
    operation = '+'
    for i, char in enumerate(s):
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        if char in "+-*/" or i == len(s) - 1:
            if operation == '+':
                stack.append(current_num)
            elif operation == '-':
                stack.append(-current_num)
            elif operation == '*':
                stack.append(stack.pop() * current_num)
            elif operation == '/':
                stack.append(int(stack.pop() / current_num))
            operation = char
            current_num = 0
    return sum(stack)
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the length of the string
- **Space Complexity**: $O(n)$, for the stack

</details>

## Exercise 9: Largest Rectangle in Histogram

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

```python
def largest_rectangle_area(heights: List[int]) -> int:
    """
    :param heights: list of bar heights
    :return: area of the largest rectangle
    """
    pass
```

<h3> Examples </h3>

```shell
Input: heights = [2,1,5,6,2,3]
Output: 10

Input: heights = [2,4]
Output: 4
```

<details>
<summary>Tests</summary>

```python
def test_largest_rectangle_area():
    assert largest_rectangle_area([2,1,5,6,2,3]) == 10
    assert largest_rectangle_area([2,4]) == 4
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_largest_rectangle_area_edge_cases():
    assert largest_rectangle_area([1,1,1,1]) == 4
    assert largest_rectangle_area([6,2,5,4,5,1,6]) == 12
    assert largest_rectangle_area([2,1,2]) == 3
```

</details>

<details>
<summary>Solution Code</summary>

```python
def largest_rectangle_area(heights: List[int]) -> int:
    stack = []
    max_area = 0
    heights.append(0)  # Add a sentinel value to pop all elements
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the number of bars
- **Space Complexity**: $O(n)$, for the stack

</details>

## Exercise 10: Asteroid Collision

We are given an array `asteroids` of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Return the state of the asteroids after all collisions.

```python
def asteroid_collision(asteroids: List[int]) -> List[int]:
    """
    :param asteroids: list of asteroids
    :return: state of asteroids after collisions
    """
    pass
```

<h3> Examples </h3>

```shell
Input: asteroids = [5, 10, -5]
Output: [5, 10]

Input: asteroids = [8, -8]
Output: []

Input: asteroids = [10, 2, -5]
Output: [10]
```

<details>
<summary>Tests</summary>

```python
def test_asteroid_collision():
    assert asteroid_collision([5, 10, -5]) == [5, 10]
    assert asteroid_collision([8, -8]) == []
    assert asteroid_collision([10, 2, -5]) == [10]
```

</details>

<details>
<summary>Hidden Tests</summary>

```python
def test_asteroid_collision_edge_cases():
    assert asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    assert asteroid_collision([1, -1, 1, -1]) == []
    assert asteroid_collision([1, 2, 3, -3, -2, -1]) == []
```

</details>

<details>
<summary>Solution Code</summary>

```python
def asteroid_collision(asteroids: List[int]) -> List[int]:
    stack = []
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the number of asteroids
- **Space Complexity**: $O(n)$, for the stack

</details>
