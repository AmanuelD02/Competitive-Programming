from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(lambda : defaultdict(int))
        for s, d, t in times:
            graph[s][d] = t
        
        Time = 0
        heap, visited = [], set()
        heap.append((0, K))
        while heap:
            time, node = heappop(heap)
            if node in visited: 
                continue
            visited.add(node)
            Time = max(Time, time)
            for neigh in graph[node]:
                if neigh not in visited:
                    heappush(heap, (time + graph[node][neigh], neigh))
        
        if len(visited) == N:
            return Time
        return -1
                    
            
            
        
        
            
        
        