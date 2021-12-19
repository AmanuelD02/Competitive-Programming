    # https://leetcode.com/problems/max-number-of-k-sum-pairs/
from collections import defaultdict
from typing import *

class Solution:
    def maxOperations(self, nums, k: int) -> int:
        visited = defaultdict(int)
        total = 0
        for i in range(len(nums)):
            target = k - nums[i]
            if target in visited:
                visited[target] -= 1
                if visited[target] ==0:
                    visited.pop(target)
                total +=1
            else:
                
                visited[(nums[i])] +=1
                    
        return total
        