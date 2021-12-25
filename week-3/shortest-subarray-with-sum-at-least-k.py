# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSum = [0] * (len(nums) +1)
        queue = deque()
        shortest = float("inf")
        
        for i in range(len(nums)):
            preSum[i+1] = preSum[i] + nums[i]
            
            
        for i in range(len(preSum)):
            while queue and preSum[i] <= preSum[queue[-1]]:
                queue.pop()
                
            queue.append(i)
            while queue and preSum[i] - preSum[queue[0]] >=k:
                shortest = min(shortest,i - queue.popleft() )
                
                
        # print(shortest)
        return shortest if shortest <= len(nums) else -1
                         
                         
