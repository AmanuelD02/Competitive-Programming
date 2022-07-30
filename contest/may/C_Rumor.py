import sys
sys.setrecursionlimit(2000)
n, m = list(map(int, input().split()))

golds = list(map(int, input().split()))

parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(node1, node2):
    p1 = find(node1)
    p2 = find(node2)
    if parent[p1] != parent[p2]:
        a, b = sorted([p1, p2], key = lambda x: golds[x])

        parent[b] = a


for i in range(m):
    a, b = list(map(int, input().split()))
    union(a-1, b-1)


answer = 0
for i in range(n):
    if find(i) == i:
        answer += golds[i]
print(answer)