class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        dist = [0] * n
        graph = defaultdict(set)
        inDegree = defaultdict(int)
        
        for pre, nex in relations:
            graph[pre].add(nex)
            inDegree[nex] += 1

        queue = deque()
        
        for k in range(1,n+1):
            v = inDegree[k]
            
            if v == 0:
                # heappush(heap, (time[k-1], k ))
                queue.append(k)
                dist[k-1] = time[k-1]
                
                
        while queue:
            item = queue.popleft()
            
            for n in graph[item]:
                inDegree[n] -= 1
                dist[n-1] = max(dist[n-1], time[n-1] + dist[item-1])
                if inDegree[n] == 0:
                    # heappush(heap, (time[n-1] + t, n))
                    queue.append(n)
                
        return max(dist)
        
                
            
        
            
        
        