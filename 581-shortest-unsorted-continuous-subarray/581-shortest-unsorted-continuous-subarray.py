class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        stack = []
        startInd,endIndx = len(nums) -1, 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                unsorted = stack.pop()
                startInd = min(startInd, unsorted)
                # print(startInd, endIndx)
            stack.append(i)
        stack = []
        for i, num in enumerate(reversed(nums)):
            
            while stack and nums[stack[-1]] < num:
                unsorted = stack.pop()
                endIndx = max(endIndx, unsorted)
            stack.append( N -1-i)
        return endIndx - startInd + 1 if endIndx - startInd > 0 else 0 