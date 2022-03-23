class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0 , x
        while left <=right:
            best = left + (right - left)//2
            if best**2== x:
                return best
            if best**2 > x:
                right = best -1
            else:
                left = best +1
        
        return right