class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(level, indx):
            if memo.get((level, indx)) is not None:
                return memo[(level, indx)]
            if level == len(triangle)-1:
                memo[(level, indx)] = triangle[level][indx]
                return memo[(level, indx)]
            
            zero = dp(level+1, indx)
            one = dp(level+1,  indx+1)
            memo[(level, indx)] = triangle[level][indx] + min(one, zero)
            
            return memo[(level, indx)]
        
        return dp(0,0)
            