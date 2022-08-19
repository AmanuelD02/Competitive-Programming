class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def helper(rate):
            count = 0
            for pile in piles:
                count += ceil(pile/rate)
                
            return count
        total = max(piles)
        left, right = 1, total
        best = -1
        while left <= right:
            rate = (left + right) //2
            if helper(rate) <=h:
                right = rate -1
                best = rate
            else:
                left = rate + 1
                
        return best
    
    