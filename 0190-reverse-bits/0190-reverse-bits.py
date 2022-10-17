class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = []
        while n:
            c = n & 1
            reversed.append(str(c))
            n = n >> 1
        for i in range(len(reversed),  32):
            reversed.append("0")
        return int("".join(reversed), 2)
        
        
        
            