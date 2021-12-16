# https://leetcode.com/problems/reduce-array-size-to-the-half/
from collections import defaultdict
class Solution:
    def minSetSize(self, arr) -> int:
        half = len(arr)//2
        total = 0
        length =0
        freq = defaultdict(int)
        for i in arr:
            freq[i] +=1
        lst =sorted(freq.items(),key= lambda x:x[1])
        for i in range(len(lst)-1,-1,-1):
            total += lst[i][1]
            length +=1
            if total >= half:
                break
        return length
            
        