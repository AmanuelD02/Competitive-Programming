class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = 0
        for i in range(1, 33):
            c = n & 1
            reversed +=  c * (2**(32 - i))
            n = n >> 1
        return reversed
        
        
            