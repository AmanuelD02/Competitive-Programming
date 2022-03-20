class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        res = cnt1 = cnt2 = 0
        for i in text:
            if i == pattern[1]:
                res += cnt1
                cnt2 +=1
            if i ==pattern[0]:
                cnt1 +=1
        return res + max(cnt2 , cnt1)
    