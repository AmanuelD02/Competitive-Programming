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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        dsu = UnionFind(N)
        ownership = {}
        
        for i, (_,*emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    dsu.union(i, ownership[email])
                ownership[email] = i
        
        lsts = defaultdict(list)
        for email, i in ownership.items():
            lsts[dsu.find(i)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in lsts.items()]
