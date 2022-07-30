class UnionFind:
    def __init__(self,size):
        self.parent = list(range(size))
        self.rank = [1] * size
        
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 != parent2:
            parent1, parent2 = sorted([parent1, parent2], key= lambda x: self.rank[x])
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
            self.rank[parent1] = 0



N, con = list(map(int, input().split()))

dsu = UnionFind(N+1)
max_rank = 0
for i in range(con):
    a, b =  list(map(int, input().split()))
    dsu.union(a,b)
    max_rank = max(max_rank, dsu.rank[dsu.find(a)] -1)
    print(max_rank)
    print(dsu.parent)
    print(dsu.rank)