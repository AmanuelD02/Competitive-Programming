class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        N = len(rides)
        rides.sort()
        
        def nextIndex(currentIndex):
            start_time = rides[currentIndex][1]
            left, right = currentIndex + 1, N - 1
            nextI = N
            while left <= right:
                mid = (left + right) >> 1
                val = rides[mid][0]
                if val >= start_time:
                    right = mid - 1
                    nextI = mid
                else:
                    left = mid + 1
            
            return nextI
        
        @lru_cache(None)
        def dp(i):
            if i >= N:
                return 0
            
            not_pick = dp(i + 1)
            pick = (rides[i][1] - rides[i][0] + rides[i][2]) + dp(nextIndex(i) )
            
            return max(pick, not_pick)
        
        return dp(0)
            