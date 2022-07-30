from bisect import bisect_left
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        ans = float('inf')
        
        sum1 = []
        sum2 = []
        
        def dfs(res, index = 0, Sum = 0,end = len(nums)-1 ):
            if index > end:  
                res.append(Sum)
                return
            pick = dfs(index = index + 1,  Sum = Sum + nums[index], end = end, res = res)
            not_picked = dfs(index = index + 1, Sum = Sum, end = end, res = res)
            
            
        
        dfs(end = len(nums)//2-1, res=sum1)
        dfs(index= len(nums)//2, res= sum2)
        
        sum2.sort()
        for i in sum1:
            t = goal - i
            j = bisect_left(sum2,t)
            if j< len(sum2):
                ans = min(ans, abs( sum2[j] + i - goal))
            if j > 0:
                ans = min(ans, abs( sum2[j-1] + i - goal))
        return ans