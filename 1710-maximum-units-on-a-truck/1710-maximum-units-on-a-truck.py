class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1])
        total = 0
        for box, unit in reversed(boxTypes):
            total += (min(truckSize, box)*unit)
            truckSize -= box
            truckSize = max(truckSize, 0)
        return total
                
        