# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n ==1:
            return True
        if n%3 !=0 or n <3:
            return False

        if n ==3:
            return True

        else:
            return self.isPowerOfThree(n/3)
            
        
        