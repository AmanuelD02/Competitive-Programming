class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        taken = []
        steps, max_num = 0, max(nums) + len(nums)
        
        for i in range(0, max_num + 1):
            if counter[i] == 0 and taken:
                steps += (i -  taken.pop())
            elif counter[i] > 1:
                taken.extend([i] * (counter[i] -1))
        
        
        return steps
                
        
        