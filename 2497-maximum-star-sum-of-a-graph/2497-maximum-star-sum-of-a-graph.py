class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        N = len(vals)
        if not edges:
            return max(vals)
        
        for a, b in edges:
            if vals[b] > 0: heappush(graph[a], (-vals[b]))
            if vals[a] > 0: heappush(graph[b], (-vals[a]))
        
        maxStar = -float("inf")

        for node in range(N):

            total = vals[node]
            count = k
            
            while graph[node] and count:
                total += (-heappop(graph[node]))    
                count -= 1
                
            maxStar = max(maxStar, total)
            
        
        return maxStar

