from typing import Counter


class Solution:
    def numIdenticalPairs(self, nums) -> int:


        ans = Counter(nums)
        sol = 0
   
        for i in ans:

            sol += (ans[i] * ans[i]-1)/2
        return sol
        