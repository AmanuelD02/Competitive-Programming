from collections import defaultdict
from heapq import heapify, heappop, heappush

n, m = list(map(int, input().split()))


graph = defaultdict(list)
visited = set()
for edges  in range(m):
    a,b = list(map(int, input().split()))
    heappush(graph[a], b)
    heappush(graph[b], a)


ans = []
visted = set()

PQ = [1]
visited.add(1)
while PQ:
    cur = heappop(PQ)
    for i in graph[cur]:
        if i not in visited:
            visited.add(i)
            heappush(PQ, i)
    ans.append(cur)


for i in ans:
    print(i, end=" ")