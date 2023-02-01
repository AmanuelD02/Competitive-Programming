class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant = list(zip(growTime, plantTime))
        plant.sort(reverse = True)
        
        res = time = 0
        
        
        for grow, p in plant:
            time += p
            res = max(res, time + grow)
        
        return res