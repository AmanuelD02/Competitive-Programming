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
                                 
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = UnionFind(len(s))
        for i, j in pairs:
            dsu.union(dsu.find(i),dsu.find(j))
        bucket = {}
        for i, j  in enumerate(dsu.parent):
            if dsu.find(j) not in bucket:
                bucket[dsu.find(j)] = []
            heappush(bucket[dsu.find(j)], s[i] )
                            
        ans = []
       
        for i, j in enumerate(dsu.parent):
            ans.append( heappop(bucket[dsu.find(j)]))
        
        return "".join(ans)