# https://leetcode.com/problems/h-index/
from typing import *
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counting = [0]* (len(citations) +1)
         
        for c in citations:
            if c > len(citations):
                counting[len(citations)] +=1
            else:
                counting[c] +=1
        
        
        total =0
        for i in range(len(counting) -1, -1,-1):
            total += counting[i]
            if total >= i:
                return i
        
        return 0
            
                    
                