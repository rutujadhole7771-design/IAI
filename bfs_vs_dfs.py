from collections import deque

# Graph
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
    nodes_expanded = 0

    while queue:

        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == target:
            return nodes_expanded

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_expanded


# ---------------- DFS ----------------

def DFS(start, target):

    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:

        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == target:
            return nodes_expanded

        for neighbour in graph[current]:
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# ---------------- Main ----------------

start = 0
target = 8

print("========== BFS ==========")
print("Nodes Expanded:", BFS(start, target))

print("\n========== DFS ==========")
print("Nodes Expanded:", DFS(start, target))