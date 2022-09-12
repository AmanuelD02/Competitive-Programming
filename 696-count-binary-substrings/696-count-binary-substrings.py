class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prefix = []
        count = 1
        for i in range(len(s)-1):
            if s[i] !=s[i+1]:
                prefix.append(count)
                count = 1
            else:
                count += 1
        prefix.append(count)
        res = 0
        for i in range(len(prefix)-1):
            res += min(prefix[i], prefix[i+1])
        
        return res