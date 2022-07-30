class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        
        heapify(stones)
        while len(stones) >=2:
            a = - heappop(stones)
            b = - heappop(stones)
            if a !=b:
                heappush(stones, b - a)
        
        if len(stones):
            return -heappop(stones)
        
        return 0 
                