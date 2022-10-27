class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            x = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)
        if p1 == p2:
            return True
        p1, p2 = sorted([p1, p2], key= lambda x: self.rank[x])
        
        self.parents[p1] = p2
        self.rank[p2] += self.rank[p1]
        
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = UnionFind(1001)
        for a, b in edges:
            if union.find(a) == union.find(b):
                return [a, b]
            union.union(a, b)
        return []