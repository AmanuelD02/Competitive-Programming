class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        length = 0
        in_bound = lambda l, r: 0 <= l and  r < len(s)
        #odd
        for i in range(len(s)):
            l = r = i
            while in_bound(l,r) and s[l] == s[r]:
                if length < (r - l + 1):
                    longest = s[l:r + 1]
                    length = r - l + 1
                l -= 1 
                r += 1
        #even
            l, r= i, i + 1
            while in_bound(l,r) and s[l] ==s[r]:
                if length < (r - l + 1):
                    longest = s[l:r + 1]
                    length = r - l + 1
                l -= 1
                r += 1
        return longest
            