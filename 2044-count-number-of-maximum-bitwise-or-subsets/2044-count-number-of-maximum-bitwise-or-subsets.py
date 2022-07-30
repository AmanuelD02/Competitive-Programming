class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        total, N = 0, len(nums)
        goal =0
        for x in nums: goal |= x
            
        for i in range(2**N):
            subset = 0
            index = 0
            while i:
                if i&1:
                    subset |= nums[index]
                i >>= 1
                index += 1
            if subset == goal: total += 1
        
        return total