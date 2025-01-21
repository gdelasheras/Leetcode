<h1> Hash Exercises </h1>

<h2> Table of Contents </h2>

- [Exercise 1: First Unique Character](#exercise-1-first-unique-character)
- [Exercise 2: Valid Sudoku](#exercise-2-valid-sudoku)
- [Exercise 3: Valid Anagram](#exercise-3-valid-anagram)
- [Exercise 4: Group Anagrams](#exercise-4-group-anagrams)
- [Exercise 5: Subarray Sum Equals K](#exercise-5-subarray-sum-equals-k)
- [Exercise 6: Longest Consecutive Sequence](#exercise-6-longest-consecutive-sequence)
- [Exercise 7: LRU Cache](#exercise-7-lru-cache)
- [Exercise 8: Time-Based Key-Value Store](#exercise-8-time-based-key-value-store)
- [Exercise 9: Minimum Window Substring](#exercise-9-minimum-window-substring)
- [Exercise 10: Design Twitter](#exercise-10-design-twitter)
- [Exercise 11: Design In-Memory File System](#exercise-11-design-in-memory-file-system)

## Exercise 1: First Unique Character

Given a string `s`, find the first non-repeating character and return its index. If it doesn't exist, return `-1`.

```python
def first_unique_char(s: str) -> int:
    """
    :param s: input string
    :return: index of first unique character, -1 if none exists
    """
    pass
```

<h3> Examples </h3>

```shell
Input: s = "leetcode"
Output: 0
Explanation: 'l' is the first character that appears only once.

Input: s = "loveleetcode"
Output: 2
Explanation: 'v' is the first character that appears only once.
```

<h3> Tests </h3>

```python
def test_first_unique_char():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
```

<details>
<summary>Hidden Tests</summary>

```python
def test_first_unique_char_edge_cases():
    assert first_unique_char("") == -1
    assert first_unique_char("a") == 0
    assert first_unique_char("aaaaaaaaa") == -1
    assert first_unique_char("abcdefghijklmnopqrstuvwxyz") == 0
    # Test with 10000 character string
    assert first_unique_char("a" * 9999 + "b") == 9999
```

</details>

<details>
<summary>Solution Code</summary>

```python
def first_unique_char(s: str) -> int:
    char_count = {}

    # Count character frequencies
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find first character with count 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the length of the string
  - First pass to count frequencies: $O(n)$
  - Second pass to find first unique: $O(n)$
- **Space Complexity**: $O(k)$, where $k$ is the size of the character set
  - In practice, `k ≤ 26` for lowercase English letters, so $O(1)$

The hash map is essential here as it allows us to count frequencies in linear time and perform constant-time lookups when checking counts.

</details>

## Exercise 2: Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

```python
def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
    :param board: 9x9 Sudoku board
    :return: true if board is valid, false otherwise
    """
    pass
```

<h3> Examples </h3>

```shell
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as first board except first "5" is changed to "8". Since there are two 8's in the first column, it is invalid.
```

<h3> Tests </h3>

```python
def test_is_valid_sudoku():
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku(valid_board) == True

    invalid_board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku(invalid_board) == False
```

<details>
<summary>Hidden Tests</summary>

```python
def test_is_valid_sudoku_edge_cases():
    # Empty board (all dots)
    empty_board = [["." for _ in range(9)] for _ in range(9)]
    assert is_valid_sudoku(empty_board) == True

    # Full valid board
    full_board = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    assert is_valid_sudoku(full_board) == True

    # Invalid box
    invalid_box_board = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","5"]  # Last digit changed to 5
    ]
    assert is_valid_sudoku(invalid_box_board) == False
```

</details>

<details>
<summary>Solution Code</summary>

```python
def is_valid_sudoku(board: List[List[str]]) -> bool:
    # Initialize sets to keep track of numbers in each row, column and box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue

            # Calculate box index
            box_idx = (i // 3) * 3 + j // 3

            # Check if number already exists in row, column or box
            if (num in rows[i] or
                num in cols[j] or
                num in boxes[box_idx]):
                return False

            # Add number to sets
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_idx].add(num)

    return True
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(1)$ since we're always iterating through a 9x9 board
  - In general terms, it would be $O(n^2)$ for an n×n board
- **Space Complexity**: $O(1)$ since we're using fixed-size sets
  - In general terms, it would be $O(n^2)$ for an n×n board

Hash sets are crucial here as they provide $O(1)$ lookups when checking for duplicates in rows, columns, and boxes.

</details>

## Exercise 3: Valid Anagram

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

```python
def is_anagram(s: str, t: str) -> bool:
    """
    :param s: first string
    :param t: second string
    :return: true if strings are anagrams, false otherwise
    """
    pass
```

<h3> Examples </h3>

```shell
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

<h3> Tests </h3>

```python
def test_is_anagram():
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
```

<details>
<summary>Hidden Tests</summary>

```python
def test_is_anagram_edge_cases():
    assert is_anagram("", "") == True
    assert is_anagram("a", "a") == True
    assert is_anagram("ab", "ba") == True
    assert is_anagram("abc", "cba") == True
    assert is_anagram("abc", "def") == False
    assert is_anagram("a" * 10000, "a" * 10000) == True
    assert is_anagram("a" * 10000, "b" * 10000) == False
```

</details>

<details>
<summary>Solution Code</summary>

```python
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n~log~n)$, where $n$ is the length of the strings
  - Sorting both strings takes $O(n~log~n)$ time
- **Space Complexity**: $O(1)$
  - Sorting is done in-place and uses constant extra space

</details>

## Exercise 4: Group Anagrams

Given an array of strings `strs`, group the anagrams together. Return the answer in any order.

```python
def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    :param strs: list of strings
    :return: list of grouped anagrams
    """
    pass
```

<h3> Examples </h3>

```shell
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]
```

<h3> Tests </h3>

```python
def test_group_anagrams():
    assert sorted(map(sorted, group_anagrams(["eat","tea","tan","ate","nat","bat"]))) == \
           sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
```

<details>
<summary>Hidden Tests</summary>

```python
def test_group_anagrams_edge_cases():
    # Empty input
    assert group_anagrams([]) == []

    # All same strings
    assert len(group_anagrams(["a"] * 1000)) == 1

    # No anagrams
    result = group_anagrams(["abc", "def", "ghi"])
    assert all(len(group) == 1 for group in result)

    # Large strings
    large_strs = ["a" * 100 + str(i) for i in range(100)]
    assert len(group_anagrams(large_strs)) == 100
```

</details>

<details>
<summary>Solution Code</summary>

```python
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)

    for s in strs:
        # Create a key by sorting characters
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)

    return list(anagram_groups.values())
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $ O(n~k~log~k) $, where:
  - $ n $ is the number of strings
  - $ k $ is the maximum length of a string
  - The sorting of each string takes $ O(k~log~k) $
- **Space Complexity**: $ O(n~k) $
  - We store all strings in our hash map

A hash map is crucial here as it allows us to group strings with the same sorted character sequence together efficiently.

</details>

## Exercise 5: Subarray Sum Equals K

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

```python
def subarray_sum(nums: List[int], k: int) -> int:
    """
    :param nums: list of integers
    :param k: target sum
    :return: number of subarrays with sum k
    """
    pass
```

<h3> Examples </h3>

```shell
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: [1,1] appears twice as subarray

Input: nums = [1,2,3], k = 3
Output: 2
Explanation: [1,2] and [3] both sum to 3
```

<h3> Tests </h3>

```python
def test_subarray_sum():
    assert subarray_sum([1,1,1], 2) == 2
    assert subarray_sum([1,2,3], 3) == 2
    assert subarray_sum([1], 1) == 1
```

<details>
<summary>Hidden Tests</summary>

```python
def test_subarray_sum_edge_cases():
    assert subarray_sum([], 0) == 0
    assert subarray_sum([0,0,0], 0) == 6
    assert subarray_sum([-1,-1,1], 0) == 1
    # Large input
    assert subarray_sum([1]*10000, 5) > 0
    # Test with negative numbers
    assert subarray_sum([1,-1,1,-1], 0) == 4
```

</details>

<details>
<summary>Solution Code</summary>

```python
def subarray_sum(nums: List[int], k: int) -> int:
    count = 0
    curr_sum = 0
    sum_freq = {0: 1}  # Initialize with 0 sum having frequency 1

    for num in nums:
        curr_sum += num

        # If (curr_sum - k) exists in map, add its frequency to count
        if curr_sum - k in sum_freq:
            count += sum_freq[curr_sum - k]

        # Update frequency of current sum
        sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1

    return count
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where n is the length of nums
  - Single pass through the array
- **Space Complexity**: $O(n)$
  - Hash map can store up to n different prefix sums

The hash map is essential here to keep track of prefix sums and their frequencies, allowing us to find subarrays with sum k in linear time.

</details>

## Exercise 6: Longest Consecutive Sequence

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

```python
def longest_consecutive(nums: List[int]) -> int:
    """
    :param nums: list of integers
    :return: length of longest consecutive sequence
    """
    pass
```

<h3> Examples </h3>

```shell
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1,2,3,4]

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

<h3> Tests </h3>

```python
def test_longest_consecutive():
    assert longest_consecutive([100,4,200,1,3,2]) == 4
    assert longest_consecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert longest_consecutive([]) == 0
```

<details>
<summary>Hidden Tests</summary>

```python
def test_longest_consecutive_edge_cases():
    assert longest_consecutive([1]) == 1
    assert longest_consecutive([1,1,1,1]) == 1
    # Test with negative numbers
    assert longest_consecutive([-5,-4,-3,-2,-1]) == 5
    # Large sequence with gaps
    large_nums = list(range(0, 10000, 2))  # Even numbers
    assert longest_consecutive(large_nums) == 1
    # Duplicate numbers
    assert longest_consecutive([1,2,2,3,3,4,4]) == 4
```

</details>

<details>
<summary>Solution Code</summary>

```python
def longest_consecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(n)$, where $n$ is the length of nums
  - Although we have nested loops, each number is only visited once
- **Space Complexity**: $O(n)$
  - We store all numbers in a hash set

A hash set is crucial here as it provides $O(1)$ lookups when checking for consecutive numbers.

</details>

## Exercise 7: LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity.
- `int get(int key)` Return the value of the key if it exists, otherwise return -1.
- `void put(int key, int value)` Update the value of the key if it exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity, evict the least recently used key.

```python
class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
```

<h3> Examples </h3>

```shell
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]
```

<h3> Tests </h3>

```python
def test_lru_cache():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
```

<details>
<summary>Hidden Tests</summary>

```python
def test_lru_cache_edge_cases():
    # Test with capacity 1
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2

    # Test updating existing key
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 2)
    assert cache.get(1) == 2

    # Test large number of operations
    cache = LRUCache(3)
    for i in range(1000):
        cache.put(i, i)
        if i >= 3:
            assert cache.get(i-3) == -1
```

</details>

<details>
<summary>Solution Code</summary>

```python
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.head = Node()  # dummy head
        self.tail = Node()  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        # Always add after head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove from tail
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(1)$ for both get and put operations
  - Hash map provides $O(1)$ access
  - Doubly linked list operations are $O(1)$
- **Space Complexity**: $O(capacity)$
  - Storage limited by cache capacity

This implementation uses a hash map for $O(1)$ lookups and a doubly linked list for $O(1)$ removal/addition of nodes, making it optimal for LRU cache operations.

</details>

## Exercise 8: Time-Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

```python
class TimeMap:
    """
    set(key: str, value: str, timestamp: int) stores key, value at the given timestamp
    get(key: str, timestamp: int) returns value at timestamp or earlier (empty string if none)
    """
    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass
```

<h3> Examples </h3>

```shell
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output:
[null, null, "bar", "bar", null, "bar2", "bar2"]
```

<h3> Tests </h3>

```python
def test_time_map():
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"
    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"
```

<details>
<summary>Hidden Tests</summary>

```python
def test_time_map_edge_cases():
    time_map = TimeMap()
    # Test non-existent key
    assert time_map.get("notfound", 1) == ""

    # Test timestamp before any values
    time_map.set("key", "value", 100)
    assert time_map.get("key", 50) == ""

    # Test multiple values for same key
    time_map.set("key", "value1", 1)
    time_map.set("key", "value2", 2)
    time_map.set("key", "value3", 3)
    assert time_map.get("key", 2) == "value2"
    assert time_map.get("key", 2.5) == "value2"

    # Test large timestamps
    time_map.set("key", "value", 1000000)
    assert time_map.get("key", 999999) == "value3"
```

</details>

<details>
<summary>Solution Code</summary>

```python
from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> list of (timestamp, value) pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        idx = bisect.bisect(values, (timestamp, chr(127)))

        if idx == 0:
            return ""
        return values[idx - 1][1]
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**:
  - set: $O(1)$
  - get: $O(log~n)$ where $n$ is the number of timestamps for the key
- **Space Complexity**: $O(n)$ where $n$ is total number of key-value pairs

A hash map is used to store the time series data for each key, while binary search helps find the closest timestamp efficiently.

</details>

## Exercise 9: Minimum Window Substring

Given two strings `s` and `t`, return the minimum window substring of `s` that contains all characters of `t`. If no such substring exists, return empty string.

```python
def min_window(s: str, t: str) -> str:
    """
    :param s: source string
    :param t: target string
    :return: minimum window substring containing all characters of t
    """
    pass
```

<h3> Examples </h3>

```shell
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"
```

<h3> Tests </h3>

```python
def test_min_window():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
```

<details>
<summary>Hidden Tests</summary>

```python
def test_min_window_edge_cases():
    # Empty strings
    assert min_window("", "") == ""
    assert min_window("", "a") == ""

    # No solution
    assert min_window("abc", "d") == ""

    # Entire string is solution
    assert min_window("abc", "abc") == "abc"

    # Multiple solutions, should return shortest
    assert min_window("aaaaabaab", "ab") in ["ab", "ba"]

    # Large strings
    s = "a" * 10000 + "b" + "a" * 10000
    assert len(min_window(s, "b")) == 1
```

</details>

<details>
<summary>Solution Code</summary>

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    # Dictionary to keep count of all the unique characters in t
    dict_t = Counter(t)
    required = len(dict_t)

    # Filter s to include only characters in t
    filtered_s = [(i, char) for i, char in enumerate(s) if char in dict_t]

    # Left and right pointer
    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    while r < len(filtered_s):
        char = filtered_s[r][1]
        window_counts[char] = window_counts.get(char, 0) + 1

        if window_counts[char] == dict_t[char]:
            formed += 1

        # Try to contract the window
        while l <= r and formed == required:
            char = filtered_s[l][1]

            # Save smallest window
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[char] -= 1
            if window_counts[char] < dict_t[char]:
                formed -= 1
            l += 1

        r += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**: $O(|S| + |T|)$ where $|S|$ and $|T|$ are lengths of strings
  - Counter creation: $O(|T|)$
  - Processing each character: $O(|S|)$
- **Space Complexity**: $O(|S| + |T|)$
  - Hash maps for counting: $O(|T|)$
  - Filtered array: $O(|S|)$

Hash maps are essential for tracking character frequencies and enabling efficient window validation.

</details>

## Exercise 10: Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and see the 10 most recent tweets in the user's news feed.

```python
class Twitter:
    """
    postTweet(userId, tweetId): Composes a new tweet
    getNewsFeed(userId): Retrieves 10 most recent tweets in user's feed
    follow(followerId, followeeId): followerId follows followeeId
    unfollow(followerId, followeeId): followerId unfollows followeeId
    """
    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass
```

<h3> Examples </h3>

```shell
Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output:
[null, null, [5], null, null, [6, 5], null, [5]]
```

<h3> Tests </h3>

```python
def test_twitter():
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]
```

<details>
<summary>Hidden Tests</summary>

```python
def test_twitter_edge_cases():
    twitter = Twitter()

    # Test empty feed
    assert twitter.getNewsFeed(1) == []

    # Test following yourself
    twitter.follow(1, 1)
    twitter.postTweet(1, 1)
    assert twitter.getNewsFeed(1) == [1]

    # Test multiple tweets
    for i in range(15):
        twitter.postTweet(1, i)
    feed = twitter.getNewsFeed(1)
    assert len(feed) == 10
    assert feed == list(range(14, 4, -1))

    # Test multiple followers
    twitter = Twitter()
    for i in range(100):
        twitter.follow(1, i)
        twitter.postTweet(i, i)
    feed = twitter.getNewsFeed(1)
    assert len(feed) == 10
```

</details>

<details>
<summary>Solution Code</summary>

```python
from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)  # userId -> list of [timestamp, tweetId]
        self.follows = defaultdict(set)  # userId -> set of followeeIds
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Add user to their own follows
        self.follows[userId].add(userId)

        # Merge tweets from all followees
        heap = []
        for followeeId in self.follows[userId]:
            tweets = self.tweets[followeeId]
            if tweets:
                time, tweetId = tweets[-1]
                heap.append([time, tweetId, followeeId, len(tweets)-1])

        heapq.heapify(heap)
        feed = []

        while heap and len(feed) < 10:
            time, tweetId, userId, idx = heapq.heappop(heap)
            feed.append(tweetId)

            if idx > 0:
                time, tweetId = self.tweets[userId][idx-1]
                heapq.heappush(heap, [time, tweetId, userId, idx-1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # Can't unfollow yourself
            self.follows[followerId].discard(followeeId)
```

</details>

<details>
<summary>Solution Complexity</summary>

- **Time Complexity**:
  - postTweet: $O(1)$
  - getNewsFeed: $O(N~log~K)$ where $N$ is total tweets and $K$ is number of users followed
  - follow/unfollow: $O(1)$
- **Space Complexity**: $O(U + T)$ where $U$ is number of users and $T$ is total tweets

Hash maps are used to store user relationships and tweets, while a heap helps merge tweets efficiently.

</details>

## Exercise 11: Design In-Memory File System

Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

- `FileSystem()` Initializes the object of the system
- `List<String> ls(String path)` Returns all files and directories in path sorted alphabetically
- `void mkdir(String path)` Creates a new directory with the given path. The path should not exist
- `void addContentToFile(String filePath, String content)` Creates or appends content to a file
- `String readContentFromFile(String filePath)` Returns the content of the file at filePath

```python
class FileSystem:
    def __init__(self):
        pass

    def ls(self, path: str) -> List[str]:
        pass

    def mkdir(self, path: str) -> None:
        pass

    def addContentToFile(self, filePath: str, content: str) -> None:
        pass

    def readContentFromFile(self, filePath: str) -> str:
        pass
```

<h3> Examples </h3>

```shell
Input:
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output:
[null, [], null, null, ["a"], "hello"]
```

<h3> Tests </h3>

```python
def test_file_system():
    fs = FileSystem()
    assert fs.ls("/") == []
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    assert fs.ls("/") == ["a"]
    assert fs.readContentFromFile("/a/b/c/d") == "hello"
```

<details>
<summary>Hidden Tests</summary>

```python
def test_file_system_edge_cases():
    fs = FileSystem()

    # Test empty paths
    fs.mkdir("/a")
    assert fs.ls("/") == ["a"]

    # Test file operations
    fs.addContentToFile("/a/file.txt", "hello")
    assert fs.ls("/a") == ["file.txt"]
    fs.addContentToFile("/a/file.txt", " world")
    assert fs.readContentFromFile("/a/file.txt") == "hello world"

    # Test deep directories
    fs.mkdir("/a/b/c/d/e/f")
    assert len(fs.ls("/a/b/c/d/e")) == 1

    # Test multiple files in directory
    fs.addContentToFile("/a/b/file1.txt", "content1")
    fs.addContentToFile("/a/b/file2.txt", "content2")
    fs.addContentToFile("/a/b/file3.txt", "content3")
    assert len(fs.ls("/a/b")) == 4  # 3 files + 1 directory
    assert sorted(fs.ls("/a/b"))[0] == "c"

    # Test file with same name in different directories
    fs.addContentToFile("/a/test.txt", "test1")
    fs.addContentToFile("/a/b/test.txt", "test2")
    assert fs.readContentFromFile("/a/test.txt") == "test1"
    assert fs.readContentFromFile("/a/b/test.txt") == "test2"
```

</details>

<details>
<summary>Solution Code</summary>

```python
class FileNode:
    def __init__(self):
        self.children = {}  # name -> FileNode
        self.content = None  # None for directory, string for file
        self.is_file = False

class FileSystem:
    def __init__(self):
        self.root = FileNode()

    def _get_node(self, path: str) -> FileNode:
        if path == "/":
            return self.root

        components = path.split("/")[1:]  # Skip empty string before first /
        node = self.root

        for component in components:
            if component not in node.children:
                node.children[component] = FileNode()
            node = node.children[component]

        return node

    def ls(self, path: str) -> List[str]:
        node = self._get_node(path)

        if node.is_file:
            return [path.split("/")[-1]]

        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._get_node(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._get_node(filePath)
        if not node.is_file:
            node.is_file = True
            node.content = ""
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._get_node(filePath)
        return node.content
```

</details>

<details>
<summary>Solution Complexity</summary>

- ~:
  - ls: $O(n~log~n)$ where $n$ is number of items in directory (due to sorting)
  - mkdir: $O(m)$ where $m$ is the depth of the path
  - addContentToFile: $O(m + k)$ where $k$ is the length of content
  - readContentFromFile: $O(m)$
- **Space Complexity**: $O(N + M)$ where:
  - $N$ is total length of all file contents
  - $M$ is total length of all directory paths

A tree structure using hash maps at each node provides efficient path traversal and file/directory operations.
The hash map at each node enables $O(1)$ access to children while maintaining the hierarchical structure.

</details>
