class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dp(i):
            if i >= len(s):
                return 1
            
            one = dp(i+1) if s[i] != "0" else 0
            two = dp(i+2) if i + 1 < len(s) and s[i] != "0" and int(s[i:i+2]) < 27 else 0
            
            
            return one + two
        
        return dp(0)