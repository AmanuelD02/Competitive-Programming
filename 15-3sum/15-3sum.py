class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        added = set()
        for indx,i in enumerate(nums):
            visited = set()
            for jj in range(indx+1, len(nums)):
                j = nums[jj]
                if 0 - i- j in visited:
                    curAns = tuple(sorted([i,j,0-i-j]))
                    if curAns in added: continue
                    ans.append([i,j,0-i-j])
                    added.add(curAns)
                visited.add(j)
        return ans
                    
