# https://leetcode.com/problems/top-k-frequent-elements/submissions/
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        freq = defaultdict(int)
        for i in nums:
            freq[i] +=1
        
        lst =sorted(freq.items(),key= lambda x:x[1])
        
        lst = lst[-k:]
        
        lst = [x[0] for x in lst]
        return lst