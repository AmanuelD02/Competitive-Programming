class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans, occur = [], {}
        last = start = 0
        
        for a,j in enumerate(s) :
            occur[j] = a
        
        for i in range(len(s)):
            last = max(last, occur[s[i]])
            if i == last:
                ans.append(i - start +1)
                start = last +1
        
        return ans
        
        
