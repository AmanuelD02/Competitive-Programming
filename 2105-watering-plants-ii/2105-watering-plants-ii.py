class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        left, refill, right = 0, 0, n - 1
        CA, CB = capacityA, capacityB
        
        while left < right:
            if CA < plants[left]:
                CA = capacityA
                refill += 1
            CA -= plants[left]
            
            
            if CB < plants[right]:
                CB = capacityB
                refill += 1
            
            
            CB -= plants[right]
            
            left += 1
            right -= 1
        if(left == right):
            if max(CA, CB) < plants[left]:
                refill += 1
        
        return refill
            
            
        