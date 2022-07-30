class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        in_bound = lambda l, r: 0 <= l < len(s) and 0  <= r < len(s)
        
        #odd length
        for i in range(len(s)):
            l = r = i
            while in_bound(l, r) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        #even length
        for i in range(len(s) - 1):
            l =i
            r = i + 1
            while in_bound(l, r) and s[l] == s[r]:
                count += 1
                r +=1
                l -= 1
        
        return count
        
        