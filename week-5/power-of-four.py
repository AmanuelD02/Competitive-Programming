class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        
        if n <4 or n%4 !=0:
            return False
        
        if n==4:
            return True
        else:
            return self.isPowerOfFour(n/4)
        