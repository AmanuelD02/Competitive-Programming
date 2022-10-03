class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        F = max(fruits[-1][0], startPos)
        
        prefixSum = [0]* (F + 2)
        for position, fruit in fruits:
            prefixSum[position] = fruit
            
            
        for position, fruit in enumerate(prefixSum):
            if position >F: continue
            prefixSum[position] += prefixSum[position-1]
        if k ==0: return prefixSum[startPos] - prefixSum[startPos -1]
        
        maximum_fruit_harvested = 0
        
        
        # print(prefixSum)
        #left
        for i in range(k+1):
            curHarvestLeft =  prefixSum[min(F,startPos + max(0, k - (2*i)))] - prefixSum[max(startPos - i - 1,-1)]
            curHarvestRight =  prefixSum[min(F,startPos + i)] - prefixSum[max(startPos - max(0, k -2*i) - 1,-1)]

            # print(i,leftSide,rightSide,curHarvest)
            maximum_fruit_harvested = max(maximum_fruit_harvested, curHarvestLeft,curHarvestRight)
        # print(maximum_fruit_harvested)
        

        
        return maximum_fruit_harvested
        