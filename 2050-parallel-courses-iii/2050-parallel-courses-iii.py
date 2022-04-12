class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        final_t = 0
        graph = defaultdict(set)
        inDegree = defaultdict(int)
        
        for pre, nex in relations:
            graph[pre].add(nex)
            inDegree[nex] += 1

        heap = []
        for k in range(1,n+1):
            v = inDegree[k]
            
            if v == 0:
                heappush(heap, (time[k-1], k ))
                # print(time[k])
                final_t = max(final_t, time[k-1])
        

        heapify(heap)
        
        while heap:
            t, item = heappop(heap)
            
            for n in graph[item]:
                inDegree[n] -= 1
                if inDegree[n] == 0:
                    heappush(heap, (time[n-1] + t, n))
                    final_t = max(final_t, time[n-1] + t)
        
        return final_t
        
                
            
        
            
        
        