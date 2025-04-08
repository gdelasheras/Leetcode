<h1> Graphs </h1>

<h2> Table of Contents </h2>

- [Definition](#definition)
- [Visual Representation](#visual-representation)
- [Representation](#representation)
  - [Adjacency Matrix](#adjacency-matrix)
  - [Adjacency List](#adjacency-list)
- [Graph Traversal Methods](#graph-traversal-methods)
  - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
  - [Depth-First Search (DFS)](#depth-first-search-dfs)
- [Warmup Problems](#warmup-problems)
  - [Number of Islands](#number-of-islands)
  - [Dijkstra's Algorithm](#dijkstras-algorithm)
  - [Rotting Oranges](#rotting-oranges)

## Definition

A graph is a structure composed of nodes connected by edges. Graphs can be used to model relationships between objects.

Terminology:

- Node: A node is a vertex in the graph.
- Edge: An edge is a connection between two nodes.
- Weight: A weight is a value assigned to an edge.
- Adjanent node/neighbor: An adjacent node is a node that is connected to another node by an edge.
- Degree: The degree of a node is the number of edges connected to it.
- Path: A path is a sequence of nodes and edges connecting a starting node to an ending node.

Attributes:

- Directed: A directed graph is a graph where each edge has a direction.
- Undirected: An undirected graph is a graph where each edge does not have a direction.
- Weighted: A weighted graph is a graph where each edge has a weight.
- Unweighted: An unweighted graph is a graph where each edge does not have a weight.
- Cyclic: A cyclic graph is a graph that has a cycle.
- Acyclic: An acyclic graph is a graph that does not have a cycle.

## Visual Representation

```
        ┌─────┐         ┌─────┐
        │  1  │────────►│  2  │
        └─────┘         └─────┘
           │
           │
           ▼
        ┌─────┐
        │  3  │
        └─────┘
```

## Representation

In some problems, you will be given a graph in the form of an adjacency matrix or an adjacency list.

### Adjacency Matrix

```python

adj = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
    ]

```

### Adjacency List

```python

adj = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2]
    }

```

## Graph Traversal Methods

### Breadth-First Search (BFS)

```python

adj = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2]
    }

def bfs(adj, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(adj, 1)

# Output:
# 1
# 2
# 3
```

### Depth-First Search (DFS)

```python

adj = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2]
    }

def dfs(adj, start):
    visited = set()
    stack = [start]
    visited.add(start)
    while stack:
        node = stack.pop()
        print(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

dfs(adj, 1)

# Output:
# 1
# 3
# 2
```

## Warmup Problems

### Number of Islands

Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

<details>
<summary>Solution</summary>

</details>

<details>
<summary>Test Cases</summary>

</details>

<details>
<summary>Complexities</summary>

</details>

### Dijkstra's Algorithm

### Rotting Oranges
