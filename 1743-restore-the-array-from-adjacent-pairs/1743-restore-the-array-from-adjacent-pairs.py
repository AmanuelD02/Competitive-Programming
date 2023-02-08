class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        ans = []
        freq = defaultdict(int)

        for a, b in adjacentPairs:
            graph[a].add(b)
            graph[b].add(a)
            freq[a] += 1
            freq[b] += 1
        
        def dfs(node, prev):
            ans.append(node)
            
            for neigh in graph[node]:
                if neigh != prev:
                    dfs(neigh, node)
        
        
        for node, val in freq.items():
            if val == 1:
                dfs(node, None)
                break
        
        return ans
            
    