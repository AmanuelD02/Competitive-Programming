class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        stack = []
        mergeInterval = []
        for i,j in enumerate(s):
            if j == "(":
                stack.append(i)
            elif stack:
                mergeInterval.append((stack.pop(), i))
        
        if mergeInterval:
            longest = mergeInterval[0][1] - mergeInterval[0][0] + 1
        mergeInterval.sort()
        # print(mergeInterval)
        l = 0
        r = 1
        while(r < len(mergeInterval)):
            if mergeInterval[l][1] + 1 >= mergeInterval[r][0]:
                
                mergeInterval[l] = (mergeInterval[l][0], max(mergeInterval[l][1], mergeInterval[r][1] ))
                # print(max(mergeInterval[l][1], mergeInterval[r][1] ), l, mergeInterval[l])
                # print(mergeInterval)
                longest = max(longest, mergeInterval[l][1] - mergeInterval[l][0] + 1)
            else:
                l = r    
            r += 1
        
        
        return longest