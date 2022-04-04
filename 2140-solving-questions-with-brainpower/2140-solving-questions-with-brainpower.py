class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dfs(index=0):
            if index >= len(questions):
                return 0
            
            pick = dfs(index + questions[index][1] + 1) + questions[index][0]
            not_picked =  dfs(index + 1)
            
            return max(pick, not_picked)
        
        return dfs()