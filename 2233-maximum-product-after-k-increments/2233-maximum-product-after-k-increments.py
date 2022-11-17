class Solution:
    def maximumProduct(self, heap: List[int], k: int) -> int:
        heapify(heap)
        MOD = (10**9)  + 7
        for _ in range(k):
            if not heap:
                break
            
            smallest = heappop(heap)
            heappush(heap, smallest + 1)
        
        ans = 1
        for num in heap:
            ans = (ans * num) %  MOD
        
        return ans
                
        