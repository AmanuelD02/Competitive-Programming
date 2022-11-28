class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        N = len(candies)
        
        left = 0
        right = max(candies)
        best = left
        
        while left <= right:
            mid = ceil((left + right) /2)
           
            res = self.counter(candies, mid)
            if res < k:
                # best = left
                right = mid - 1
            else:
                best = mid
                left = mid + 1
        
        return best
                
    
    
    def counter(self, candies, k):
        if k == 0:
            return len(candies)
        total = 0
        for num in candies:
            total += num//k
        
        
        return total