class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        
        for h in range(12):
            for m in range(60):
                if self.countBits(h) + self.countBits(m) == turnedOn:
                    answer.append("%d:%02d" % (h, m))
        
        return answer
    
    def countBits(self, num):
        bits = 0
        while num:
            bits += (num & 1)
            num >>= 1
        return bits