class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s_size = len(s)
        
        @cache
        def dp(start = 0):
            nonlocal s_size
            if start == s_size:
                return [[]]
            
            ans = []
            
            for end in range(start + 1, s_size + 1):
                curr = s[start:end]
                if curr == curr[::-1]:
                    for result in dp(end):
                        ans.append([curr] + result)
            
            return ans

            
        return dp()
