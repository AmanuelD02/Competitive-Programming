class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        N = len(nums)
        ans = [-1] * N
        for n in range(2*N-1,-1,-1):
            n = n % N
            while stack and nums[stack[-1]] <= nums[n]:
                stack.pop()
            if stack: ans[n] = nums[stack[-1]]
            stack.append(n)
        

        
        return ans
        