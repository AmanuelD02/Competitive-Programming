class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        N = len(candies)
        
        left = 0
        right = max(candies)
        
        while left < right:
            mid = ceil((left + right) / 2)
           
            res = self.counter(candies, mid)
            if res < k:
                right = mid - 1
            else:
                left = mid
        
        return left
                
    
    
    def counter(self, candies, k):
        if k == 0:
            return len(candies)
        total = 0
        for num in candies:
            total += num//k
        
        
        return total