class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        deficit = startStation = currentGas = 0
        for i in range(len(gas)):
            currentGas += gas[i] - cost[i]
            if currentGas <0:
                startStation = i + 1
                deficit += currentGas 
                currentGas = 0
        
        if currentGas + deficit >=0:
            return startStation
        
        return -1