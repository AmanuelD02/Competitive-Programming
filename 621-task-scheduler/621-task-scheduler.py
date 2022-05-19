class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-val for key, val in freq.items()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
        
        while maxHeap or queue:
            for i in range(n + 1):
                FLAG = False
                if maxHeap:
                    curr = heapq.heappop(maxHeap)
                    FLAG = True
                    if curr + 1 < 0:
                        queue.append(curr + 1)
                if FLAG or queue: time += 1
                # print(time, queue, sep= "  ")
                    
            while queue:
                heapq.heappush(maxHeap, queue.popleft())
        
        return time