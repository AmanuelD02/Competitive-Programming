# https://leetcode.com/problems/next-greater-element-i/

from typing import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack= []
        kicked = {}
        for num in nums2:
            while stack and stack[-1] < num:
                kicked[stack.pop()] = num
            
            stack.append(num)
        result = []
        # print(stack)
        # print(kicked)
        for num in nums1:
            if num in kicked:
                result.append(kicked[num])
            else:
                result.append(-1)
        # print(result)
        return result
                
            
            