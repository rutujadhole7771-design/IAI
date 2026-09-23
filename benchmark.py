import timeit
from bfs_vs_dfs import BFS, DFS


START = 0

# Three different target nodes
BEST_TARGET = 0       # Starting node
AVERAGE_TARGET = 4    # Middle-level node
WORST_TARGET = 8      # Deeper node

NUMBER = 10000
REPEAT = 5


def benchmark(function, start, target):

    results = timeit.repeat(
        lambda: function(start, target),
        number=NUMBER,
        repeat=REPEAT
    )

    times = [(x / NUMBER) * 1000 for x in results]

    average_time = sum(times) / len(times)

    return times, average_time


# ==========================================
# BFS
# ==========================================

bfs_best, bfs_best_avg = benchmark(BFS, START, BEST_TARGET)
bfs_average, bfs_average_avg = benchmark(BFS, START, AVERAGE_TARGET)
bfs_worst, bfs_worst_avg = benchmark(BFS, START, WORST_TARGET)


# ==========================================
# DFS
# ==========================================

dfs_best, dfs_best_avg = benchmark(DFS, START, BEST_TARGET)
dfs_average, dfs_average_avg = benchmark(DFS, START, AVERAGE_TARGET)
dfs_worst, dfs_worst_avg = benchmark(DFS, START, WORST_TARGET)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n==============================================")
print("       BFS vs DFS - CASE ANALYSIS")
print("==============================================")


print("\nBFS RESULTS")
print("----------------------------------------------")

print(f"Best Case    : {bfs_best_avg:.6f} ms")
print(f"Average Case : {bfs_average_avg:.6f} ms")
print(f"Worst Case   : {bfs_worst_avg:.6f} ms")

print(f"Best Nodes    : {BFS(START, BEST_TARGET)}")
print(f"Average Nodes : {BFS(START, AVERAGE_TARGET)}")
print(f"Worst Nodes   : {BFS(START, WORST_TARGET)}")


print("\nDFS RESULTS")
print("----------------------------------------------")

print(f"Best Case    : {dfs_best_avg:.6f} ms")
print(f"Average Case : {dfs_average_avg:.6f} ms")
print(f"Worst Case   : {dfs_worst_avg:.6f} ms")

print(f"Best Nodes    : {DFS(START, BEST_TARGET)}")
print(f"Average Nodes : {DFS(START, AVERAGE_TARGET)}")
print(f"Worst Nodes   : {DFS(START, WORST_TARGET)}")


print("\n==============================================")
print("             FINAL COMPARISON")
print("==============================================")

print("\nCase          BFS Time       DFS Time")
print("----------------------------------------------")

print(f"Best          {bfs_best_avg:.6f}       {dfs_best_avg:.6f}")
print(f"Average       {bfs_average_avg:.6f}       {dfs_average_avg:.6f}")
print(f"Worst         {bfs_worst_avg:.6f}       {dfs_worst_avg:.6f}")

print("\n==============================================")