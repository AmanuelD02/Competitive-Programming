class Solution:
    def allPathsSourceTarget(self, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for i, nums in enumerate(edges):
            for ed in nums:
                graph[i].add(ed)
        
        N = len(edges) - 1
        answer = []
        def dfs(node, path):
            if node == N:
                answer.append(path[:])
                return
            
            for neigh in graph[node]:
                path.append(neigh)
                dfs(neigh, path)
                path.pop()
        
        
        
        
        dfs(0, [0])
        return answer