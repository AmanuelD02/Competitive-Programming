# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
import math
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        
        r=l=0
        ans = 0
        while r < len(nums):
            
            while min_deque and nums[min_deque[-1]] > nums[r]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] < nums[r]:
                max_deque.pop()
            min_deque.append(r)
            max_deque.append(r)
            
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                
                if nums[l] == nums[min_deque[0]]:
                    min_deque.popleft()
                
                if nums[l] == nums[max_deque[0]]:
                    max_deque.popleft()
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans
                
        
        
        
        