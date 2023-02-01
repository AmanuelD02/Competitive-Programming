class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        
        score_age = sorted([(age, score) for age, score in zip(ages, scores)])
        
        
        dp = [0] * N
        
        for i in range(N):
            dp[i] = score_age[i][1]
            
            for j in range(i):
                if score_age[j][1] <= score_age[i][1]:
                    dp[i] = max(dp[i], dp[j] + score_age[i][1])
        
        
        return max(dp)