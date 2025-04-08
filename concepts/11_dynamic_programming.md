<h1> Dynamic Programming </h1>

<h2> Table of Contents </h2>

- [Introduction](#introduction)
  - [Identify DP](#identify-dp)
  - [Tips](#tips)
    - [House Robber](#house-robber)
    - [Longest Increasing Subsequence](#longest-increasing-subsequence)
- [Example - Climbing Stairs](#example---climbing-stairs)
  - [Top-Down Approach (Memoization)](#top-down-approach-memoization)
  - [Bottom-Up Approach (Tabulation)](#bottom-up-approach-tabulation)
    - [Optimization](#optimization)
  - [Which is better?](#which-is-better)
  - [Warmup Problems](#warmup-problems)
    - [Minimum Coin Change](#minimum-coin-change)
    - [Longest Palindromic Substring](#longest-palindromic-substring)
    - [Unique Paths](#unique-paths)
    - [Unique Paths II](#unique-paths-ii)
    - [Minimum Path Sum](#minimum-path-sum)

## Introduction

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler <b>subproblems</b>. These subproblems are solved and their solutions are combined to solve the original problem. Recursion can also be used to solve these subproblems, but it can be inefficient for some problems, since it may <b>solve the same subproblem multiple times</b>.

Let's take a look at the Fibonacci sequence.

```
                  f(main_problem)
                        /\
                       /  \
                      /    \
                     /      \
        f(subproblem_a)  f(subproblem_b) <- this has been solved before
              /\
             /  \
            /    \
           /      \
f(subproblem_b)  f(subproblem_c)
      ...              ...
```

DP is the antidote for this, by storing the solutions to the subproblems, so they can be reused later. <b>Each subproblem is solved only once.</b>

### Identify DP

Two common use cases are:

- Finding the <b>optimal solution</b>
- Counting the <b>total number of ways</b> to solve a problem

### Tips

The <b>first characteristic</b> that is common in DP problems is that the problem will ask for the optimum value (maximum or minimum) of something, or the number of ways there are to do something. For example:

- What is the minimum cost of doing...
- What is the maximum profit from...
- How many ways are there to do...
- What is the longest possible...
- Is it possible to reach a certain point...

The <b>second characteristic</b> that is common in DP problems is that <b>future "decisions" depend on earlier decisions</b>. Deciding to do something at one step may affect the ability to do something in a later step. This characteristic is what makes a greedy algorithm invalid for a DP problem - we need to factor in results from previous decisions. Admittedly, this characteristic is not as well defined as the first one, and the best way to identify it is to go through some examples.

#### House Robber

[House Robber](https://leetcode.com/problems/house-robber/) is an excellent example of a dynamic programming problem. The problem description is:

> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
>
> Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

In this problem, <b>each decision will affect what options are available to the robber in the future</b>. For example, with the test case `nums = [2, 7, 9, 3, 1]`, the optimal solution is to rob the houses with `2`, `9`, and `1` money. However, if we were to iterate from left to right in a greedy manner, our first decision would be whether to rob the first or second house. 7 is way more money than 2, so if we were greedy, we would choose to rob house 7. However, this prevents us from robbing the house with 9 money. As you can see, our decision between robbing the first or second house affects which options are available for future decisions.

#### Longest Increasing Subsequence

[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) is another example of a classic dynamic programming problem. In this problem, we need to determine the length of the longest (first characteristic) subsequence that is strictly increasing. For example, if we had the input `nums = [1, 2, 6, 3, 5]`, the answer would be 4, from the subsequence `[1, 2, 3, 5]`. Again, the <b>important decision</b> comes when we arrive at the <b>6</b> - do we take it or not take it? If we decide to take it, then we get to increase our current length by 1, but it affects the future - we can no longer take the 3 or 5. Of course, with such a small example, it's easy to see why we shouldn't take it - but how are we supposed to design an algorithm that can always make the correct decision with huge inputs? Imagine if nums contained `10,000` numbers instead.

## Example - Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```

            ┌─► 1                   ┌► 1                   ┌► 1               ┌────► 2               ┌────► 2
            │ ┌───┐                 │┌───┐                 │┌───┐             │    ┌───┐             │    ┌───┐
        ┌─► 1 │   │             ┌► 1 │   │         ┌────► 2 │   │             │    │   │             │    │   │
        │ ┌───┘   │             │┌───┘   │         │    ┌───┘   │             │┌───┘   │             │┌───┘   │
    ┌─► 1 │       │    ┌─────► 2 │       │         │    │       │        ┌─► 1 │       │    ┌─────► 2 │       │
    │ ┌───┘       │    │     ┌───┘       │         │┌───┘       │        │ ┌───┘       │    │     ┌───┘       │

┌─► 1 │ │ │ │ │ ┌─► 1 │ │ ┌─► 1 │ │ │ │ │
│ ┌───┘ │ │ ┌───┘ │ │ ┌───┘ │ │ ┌───┘ │ │ ┌───┘ │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │
└───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘

```

### Top-Down Approach (Memoization)

Top down is a recursive approach that starts from the <b>main problem</b> and works its way down to the <b>subproblems</b>. To prevent solving the same subproblem multiple times, we can use a <b>memoization</b> technique, using a <b>cache</b> to store the solutions to the subproblems.

```python
def climb_stairs(n):
    cache = {}

    def climb(n):
        if n in cache:
            return cache[n]

        if n <= 2:
            return n

        cache[n] = climb(n - 1) + climb(n - 2)
        return cache[n]

    return climb(n)
```

- Time Complexity: $O(2^n)$
- Space Complexity: $O(n)$

Where n is the number of steps.

### Bottom-Up Approach (Tabulation)

Bottom up is a iterative approach that starts from the <b>subproblems</b> and works its way up to the <b>main problem</b>. The DP table is used to store the solutions to the subproblems.

```python
def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

- Time Complexity: $O(2^n)$
- Space Complexity: $O(n)$

Where n is the number of steps.

#### Optimization

An important thing to note is that we only need the previous two steps to calculate the current step. Therefore, we can optimize the space complexity to O(1).

```python
def climb_stairs(n):
    if n <= 2:
        return n

    one_step, two_steps = 1, 2

    for i in range(3, n + 1):
        current = one_step + two_steps
        one_step, two_steps = two_steps, current

    return two_steps
```

- Time Complexity: $O(n)$
- Space Complexity: $O(1)$

Where $n$ is the number of steps.

### Which is better?

Any DP algorithm can be implemented with either method, and there are reasons for choosing either over the other. However, each method has one main advantage that stands out:

- A <b>bottom-up</b> implementation's runtime is usually faster, as iteration does not have the overhead that recursion does.
- A <b>top-down</b> implementation is usually much easier to write. This is because with recursion, the ordering of subproblems does not matter, whereas with tabulation, we need to go through a logical ordering of solving subproblems.

### Warmup Problems

#### Minimum Coin Change

[Minimum Coin Change](https://leetcode.com/problems/coin-change/) is a variation of the Unique Paths problem. The problem description is:

> You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
```

- Time Complexity: $O(n \times m)$
- Space Complexity: $O(n)$

Where $n$ is the number of coins and $m$ is the amount.

#### Longest Palindromic Substring

[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) is a variation of the Unique Paths problem. The problem description is:

> Given a string s, return the longest palindromic substring in s.

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]
```

- Time Complexity: $O(n^2)$
- Space Complexity: $O(n^2)$

Where $n$ is the length of the string.

#### Unique Paths

[Unique Paths](https://leetcode.com/problems/unique-paths/) is a classic pathing problem. The problem description is:

> A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for i in range(m)]

        grid[0] = [1] * n

        for row in range(m):
            grid[row][0] = 1

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

        return grid[-1][-1]
```

- Time Complexity: $O(m \times n)$
- Space Complexity: $O(m \times n)$

Where $m$ is the number of rows and $n$ is the number of columns.

#### Unique Paths II

[Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) is a variation of the Unique Paths problem. The problem description is:

> A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?
> An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

```python
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0

        rows, cols = len(grid), len(grid[0])
        FREE, BLOCK, NO_PATH = 0, 1, 0

        grid[0][0] = 1

        for row in range(1, rows):
            if grid[row - 1][0] == 1 and grid[row][0] == FREE:
                grid[row][0] = 1
            else:
                grid[row][0] = NO_PATH

        for col in range(1, cols):
            if grid[0][col - 1] == 1 and grid[0][col] == FREE:
                grid[0][col] = 1
            else:
                grid[0][col] = NO_PATH

        for row in range(1, rows):
            for col in range(1, cols):
                if grid[row][col] == BLOCK:
                    grid[row][col] = NO_PATH
                else:
                    grid[row][col] = grid[row][col - 1] + grid[row - 1][col]

        return grid[-1][-1]
```

- Time Complexity: $O(m \times n)$
- Space Complexity: $O(m \times n)$

Where $m$ is the number of rows and $n$ is the number of columns.

#### Minimum Path Sum

[Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) is a variation of the Unique Paths problem. The problem description is:

> Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # First row
        for i in range(1, len(grid[0])):
            grid[0][i] = grid[0][i] + grid[0][i - 1]

        # First column
        for i in range(1, len(grid)):
            grid[i][0] = grid[i][0] + grid[i - 1][0]

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] = min(
                    grid[row][col] + grid[row][col - 1],
                    grid[row][col] + grid[row - 1][col],
                )

        return grid[-1][-1]
```

- Time Complexity: $O(m \times n)$
- Space Complexity: $O(m \times n)$

Where $m$ is the number of rows and $n$ is the number of columns.
