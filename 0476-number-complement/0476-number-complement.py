class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        k = 0
        while num:
            complement += (1 - (num & 1)) << k
            num = num >> 1
            k += 1
        return complement