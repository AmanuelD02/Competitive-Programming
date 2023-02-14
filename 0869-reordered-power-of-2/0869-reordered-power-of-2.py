class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        freq = Counter(str(n))
        
        for bit in range(31):
            if freq == Counter(str(1 << bit)):
                return True
        
        return False