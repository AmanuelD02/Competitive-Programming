# https://leetcode.com/problems/daily-temperatures/

from typing import *
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        
        
        def check(i,j):
            if j>= len(temperatures):
                return 0
            if temperatures[i] < temperatures[j]:
                return j-i
            elif ans[j] ==0:
                return 0
                
            return check(i, ans[j] +j)
        
        for i in range(len(temperatures)-1,-1,-1):
            if i == len(temperatures)-1:
                ans[i] =0
                continue
            if temperatures[i] < temperatures[i+1]:
                ans[i] =1
            else:
                # go to temperatures[ans[i+1]]
                ans[i] = check(i,i+ ans[i+1])
        return ans
                
                
        