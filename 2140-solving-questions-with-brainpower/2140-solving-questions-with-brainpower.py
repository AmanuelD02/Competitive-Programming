class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        for i in range(len(questions)-1,-1,-1):
            not_picked, pick = i+1, i+1 + questions[i][1]
            ans = questions[i][0]
            
            if not_picked < len(questions):
                ans = max(ans, dp[not_picked])
                
            if pick < len(questions):
                ans = max(ans, dp[pick] + questions[i][0])
                
            dp[i] = ans
        
        return dp[0]
            
    