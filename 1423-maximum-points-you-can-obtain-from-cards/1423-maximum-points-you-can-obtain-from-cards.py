class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxAns = curAns = 0
        for i in range(k):
            curAns += cardPoints[i]
        maxAns = curAns
        for i in range(k):
            curAns -= cardPoints[k-i-1]
            curAns += cardPoints[-1-i]
            maxAns = max(maxAns, curAns)
        return maxAns