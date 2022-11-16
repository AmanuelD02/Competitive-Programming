class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        N = len(plants)
        steps = 0
        curr_capacity = capacity
        
        for idx in range(N):
            if curr_capacity - plants[idx] >= 0:
                steps += 1
                curr_capacity -= plants[idx]
            else:
                curr_capacity = capacity - plants[idx]
                steps += idx + idx + 1
        
        return steps