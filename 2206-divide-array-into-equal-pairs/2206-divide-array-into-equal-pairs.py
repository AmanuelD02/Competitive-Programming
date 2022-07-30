class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counting = defaultdict(int)
        for i in nums:
            counting[i] +=1
        
        for i, j in counting.items():
            if j %2 !=0:
                return False
        return True
        
            