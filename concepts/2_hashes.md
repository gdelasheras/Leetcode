<h1> Hashes </h1>
<h2> Table of Contents </h2>

- [Definition](#definition)
- [Visual Representation](#visual-representation)
  - [Dictionary (Hash Table)](#dictionary-hash-table)
  - [Set (Hash Set)](#set-hash-set)
- [Basic Operations](#basic-operations)
- [Dictionary Implementation](#dictionary-implementation)
- [Common Dictionary Operations](#common-dictionary-operations)
- [Set Implementation and Operations](#set-implementation-and-operations)
- [Common Applications](#common-applications)
- [Pro-tips :sparkles:](#pro-tips-sparkles)
  - [Counter](#counter)
  - [Defaultdict](#defaultdict)
  - [OrderedDict](#ordereddict)
- [Warm up exercises](#warm-up-exercises)
  - [Example 1: Two Sum, unsorted array](#example-1-two-sum-unsorted-array)
  - [Example 2: First Non-Repeating Character](#example-2-first-non-repeating-character)
  - [Example 3: Group Anagrams](#example-3-group-anagrams)

## Definition

Hash tables are data structures that implement an associative array abstract data type, a structure that can map keys to values. Python implements hash tables primarily through dictionaries (`dict`) and sets (`set`).

## Visual Representation

### Dictionary (Hash Table)

```
key         →    value
-------------------------
"name"      →    "John"
"age"       →    25
"city"      →    "NYC"
"job"       →    "developer"
"is_active" →    true
```

### Set (Hash Set)

```
elements
-------------------------
"apple"
"banana"
"orange"
"grape"
```

## Basic Operations

| Operation | Dict/Set Average | Dict/Set Worst | Description                   |
| --------- | :--------------: | :------------: | ----------------------------- |
| Insert    |      $O(1)$      |     $O(n)$     | Add a new key-value pair      |
| Delete    |      $O(1)$      |     $O(n)$     | Remove a key-value pair       |
| Search    |      $O(1)$      |     $O(n)$     | Find a value by key           |
| Update    |      $O(1)$      |     $O(n)$     | Modify value for existing key |

## Dictionary Implementation

```python
class HashTable:
    def __init__(self):             # Initialize the hash table
        self.data = {}              # Use a dictionary to store data

    def set(self, key, value):      # Add or update a key-value pair
        self.data[key] = value      # Set the value for the given key

    def get(self, key):             # Retrieve the value for a given key
        return self.data.get(key)   # Return the value if key exists, else None

    def delete(self, key):          # Remove a key-value pair
        if key in self.data:        # Check if the key exists
            del self.data[key]      # Delete the key-value pair

    def exists(self, key):          # Check if a key exists in the hash table
        return key in self.data     # Return True if key exists, else False
```

## Common Dictionary Operations

```python
# Creation
empty_dict = {}
person = {"name": "John", "age": 30}
dict_from_pairs = dict([("a", 1), ("b", 2)])

# Insertion/Update
person["city"] = "NYC"        # Add new key-value
person.update({"age": 31})    # Update existing

# Access
name = person["name"]         # Direct access
age = person.get("age", 0)    # Access with default

# Deletion
del person["city"]            # Remove key
removed = person.pop("age")   # Remove and return value
person.clear()                # Remove all items

# Iteration
for key in person:                  # Iterate keys
    print(key)
for value in person.values():       # Iterate values
    print(value)
for key, value in person.items():   # Iterate pairs
    print(key, value)

# Membership
if "name" in person:        # Check key existence
```

## Set Implementation and Operations

```python
# Creation
empty_set = set()
numbers = {1, 2, 3, 4, 5}
set_from_list = set([1, 2, 2, 3])  # Duplicates removed

# Modification
numbers.add(6)          # Add single element
numbers.update([7, 8])  # Add multiple elements
numbers.remove(1)       # Remove (raises KeyError if missing)
numbers.discard(1)      # Remove (no error if missing)

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

union = a | b           # {1, 2, 3, 4, 5}
intersection = a & b    # {3}
difference = a - b      # {1, 2}
symmetric_diff = a ^ b  # {1, 2, 4, 5}
```

## Common Applications

- Caching.
- Counting/Frequency Analysis.
- Deduplication.
- Grouping/Indexing.

## Pro-tips :sparkles:

### Counter

`Counter` is a dictionary subclass that counts hashable objects. It is used to count the frequency of each element in an iterable.

```python
from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(nums)

print(counter) # Counter({4: 4, 3: 3, 2: 2, 1: 1})
```

### Defaultdict

`defaultdict` is a dictionary subclass that calls a factory function to supply missing values. It is used to initialize the dictionary with a default value for each key.

```python
from collections import defaultdict

dd = defaultdict(int)
dd['a'] = 1
dd['b'] = 2

print(dd) # defaultdict(<class 'int'>, {'a': 1, 'b': 2})

print(dd['c']) # 0
```

### OrderedDict

`OrderedDict` is a dictionary subclass that remembers the order of items inserted. It is used to maintain the order of the keys in the dictionary.

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2

print(od) # OrderedDict([('a', 1), ('b', 2)])
```

## Warm up exercises

### Example 1: Two Sum, unsorted array

Find two numbers in an unsortedarray that add up to a target.

<details>
<summary>Solution</summary>

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

</details>

<details>
<summary>Test Cases</summary>

```python
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3, 4], 8) == []
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$
- Space complexity: $O(n)$
</details>

### Example 2: First Non-Repeating Character

<details>
<summary>Solution</summary>

```python
def first_non_repeating(s):
    char_count = {}

    # Count occurrences
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find first non-repeating
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1
```

</details>

<details>
<summary>Test Cases</summary>

```python
def test_first_non_repeating():
    assert first_non_repeating("leetcode") == 0
    assert first_non_repeating("loveleetcode") == 2
    assert first_non_repeating("aabb") == -1
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n)$
- Space complexity: $O(k)$ where k is size of character set
</details>

### Example 3: Group Anagrams

<details>
<summary>Solution</summary>

```python
def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams.setdefault(sorted_s, []).append(s)
    return list(anagrams.values())
```

</details>

<details>
<summary>Test Cases</summary>

```python
assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
assert group_anagrams([""]) == [[""]]
assert group_anagrams(["a"]) == [["a"]]
assert group_anagrams(["ac", "c"]) == [["ac"], ["c"]]
```

</details>

<details>
<summary>Complexities</summary>

- Time complexity: $O(n \times k \times \log k)$
- Space complexity: $O(n \times k)$
</details>
