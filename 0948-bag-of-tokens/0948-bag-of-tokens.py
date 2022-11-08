class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        maxScore = score = 0
        left, right = 0, len(tokens) -1
        
        while left <= right:
            if power - tokens[left] >= 0:
                score += 1
                power -= tokens[left]
                left += 1
                maxScore = max(maxScore, score)            
            elif score >= 1:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
 
        return maxScore
                