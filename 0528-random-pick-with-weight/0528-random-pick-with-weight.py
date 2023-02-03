class Solution:
    def __init__(self, w: List[int]):
        self.other = []
        Sum = sum(w)
        for i in range(len(w)):
            ratio = w[i]/ Sum
            freq = ceil(ratio*(len(w)*10))
            self.other.extend([i] * freq)
        
    def pickIndex(self) -> int:
        return random.choice(self.other)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()