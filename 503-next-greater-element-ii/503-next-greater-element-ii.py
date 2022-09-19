class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        Max = nums[0]
        index = 0
        for i, num in enumerate(nums):
            if num >= Max:
                Max =num
                index = i

        nextGreaterElement= [float("inf")] * n
        nextGreaterIndex  = [-1] * n
        for i in range(index-1, -1 ,-1):
            cur= (i+1) % n
            while nums[i] >=  nums[cur]:
                if nextGreaterElement[cur]== float("inf"): break
                cur = nextGreaterIndex[cur]
            if nums[i] != nums[cur]:
                nextGreaterElement[i] = nums[cur]
            nextGreaterIndex[i] = cur
    

    
        for i in range(n-1, index,-1):
            cur= (i+1) % n 
            while nums[i] >= nums[cur]:
                if nextGreaterElement[cur]== float("inf"):
                    
                    break
                cur = nextGreaterIndex[cur]
            
            if nums[i] != nums[cur]:
                nextGreaterElement[i] = nums[cur]
            nextGreaterIndex[i] = cur
        
        for i, num in enumerate(nextGreaterElement):
            if num == float("inf"):
                nextGreaterElement[i] = -1
        
        return nextGreaterElement
            