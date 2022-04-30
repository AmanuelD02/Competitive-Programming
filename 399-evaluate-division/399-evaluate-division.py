class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1/v
        
        @lru_cache(None)
        def bfs(src, dest):
            if not(src in graph and dest in graph): return -1.0
            
            queue, visited = deque(), set()
            queue.append(((src, 1.0)))
            while queue:
                x, v=queue.popleft()
                
                if x == dest: return v
                visited.add(x)
                for i in graph[x]:
                    if i not in visited:
                        queue.append((i, v* graph[x][i]))
            return -1.0
        
        return [bfs(src, dest) for src, dest in queries]
        
                
                
        
        