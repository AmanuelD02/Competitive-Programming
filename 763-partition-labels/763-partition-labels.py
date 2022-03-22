class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = defaultdict(list)
        start = i = 0
        ans = []
        for a,j in enumerate(s) :
            occur[j].append(a)
        
        last = occur[s[0]][-1]
        while i < len(s):
            # print(i, start, last)
            if i == last:
                ans.append(i - start +1)
                start = last +1
                if start <len(s):
                    last = occur[s[start]][-1]
            else:
                last = max(last, occur[s[i]][-1])
            
            i+=1
        return ans
        
        