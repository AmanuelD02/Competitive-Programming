class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        incr = [1] * len(security)
        decr = [1] * len(security)
        
        ans = []
        # decr
        for i in range(1,len(security)):
            if security[i-1] >= security[i]:
                decr[i] = decr[i-1] + decr[i]
        # incr
        for i in range(len(security)-2,-1,-1):
            if security[i] <= security[i+1]:
                incr[i] += incr[i+1]
        
        for i in range(time, len(security) - time):
            if incr[i] > time and decr[i] > time:
                ans.append(i)
        
        return ans
        
            