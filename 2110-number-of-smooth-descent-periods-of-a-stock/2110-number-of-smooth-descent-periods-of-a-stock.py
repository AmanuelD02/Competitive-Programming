class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count, total = 1, 0
        for i in range(len(prices)-1):
            if prices[i] - prices[i+1] == 1:
                count += 1
            else:
                total += (count * (count + 1))/2 
                count = 1
        
        total += (count * (count + 1))/2
        return int(total)