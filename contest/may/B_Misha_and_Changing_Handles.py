
import sys

sys.setrecursionlimit(1 << 30)
queries = int(input())

starting = set()
visited = set()
graph  = {}
for _ in range(queries):
    u, v = input().split()
    # print(u, v)   
    if u not in visited:
        starting.add(u)
    visited.add(u)
    visited.add(v)
    graph[u] = v

def dfs(node):
    ans = node
    # print(node)

    if graph.get(node) != None:
        ans = dfs(graph[node])
    return ans
# print(graph)
# print(visited)
# print(starting)
print(len(starting))
for n in starting:
    print(n, dfs(n))
    