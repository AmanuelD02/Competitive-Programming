class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans =[]
        for i in range(len(nums)):
            while queue and i - queue[0] + 1 > k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            
            if i+1 < k: continue
            ans.append(nums[queue[0]])
        
        return ans
        
        
                
                