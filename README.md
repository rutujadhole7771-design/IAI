# SLE-2: BFS vs DFS Profiling

## Objective

The objective of this project is to compare the performance of Breadth First Search (BFS) and Depth First Search (DFS) using actual execution time and number of nodes expanded.

## Problem Statement

A small graph is used as the search problem. The graph contains nodes from **0 to 8** and connections between the nodes. BFS and DFS start from node **0** and search for the target node **8**.

### Graph Used

```text
             0
            / \
           1   2
          / \ / \
         3  4 5  6
         |       |
         7       8
```

### Graph Connections

```text
0 → 1, 2
1 → 3, 4
2 → 5, 6
3 → 7
4 → -
5 → -
6 → 8
7 → -
8 → -
```

The same graph and target node are used for both BFS and DFS so that their performance can be compared fairly.

## Files

* `bfs_vs_dfs.py` – Contains the BFS and DFS algorithms.
* `benchmark.py` – Measures execution time using Python `timeit`.
* `profilesearch.py` – Runs BFS and DFS repeatedly for py-spy profiling.

## Profiling Method

Both algorithms are executed multiple times on the same graph. The execution time is measured using `timeit`, and the average time is calculated. The number of nodes expanded by each algorithm is also recorded.

Py-spy is used to generate a profiling flame graph showing where execution time is spent.

## Case Analysis

The algorithms are considered in three cases:

* **Best Case:** Target is the starting node.
* **Average Case:** Target is located at an intermediate level.
* **Worst Case:** Target requires exploring more nodes before it is reached.

## Conclusion

The measured benchmark results are used to compare BFS and DFS. The comparison is based on actual execution time and nodes expanded for the selected graph.
