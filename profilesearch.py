from collections import deque


# ---------------- GRAPH ----------------

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [7],
    4: [],
    5: [],
    6: [8],
    7: [],
    8: []
}


# ---------------- BFS ----------------

def BFS(start, target):

    queue = deque([start])
    visited = set()

    while queue:

        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        if current == target:
            return

        for neighbour in graph[current]:

            if neighbour not in visited:
                queue.append(neighbour)


# ---------------- DFS ----------------

def DFS(start, target):

    stack = [start]
    visited = set()

    while stack:

        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == target:
            return

        for neighbour in graph[current]:

            if neighbour not in visited:
                stack.append(neighbour)


# ---------------- PROFILING WORKLOAD ----------------

print("Starting BFS and DFS profiling...")

for i in range(1000000):

    BFS(0, 8)
    DFS(0, 8)

print("BFS and DFS profiling completed.")