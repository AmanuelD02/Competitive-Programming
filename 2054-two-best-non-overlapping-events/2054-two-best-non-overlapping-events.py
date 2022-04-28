class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()
        # print(events)
        k = 2
        @lru_cache(None)
        def dp(i, k):
            if i >= N or k == 0:
                return 0
            
            left, right = i + 1, N - 1
            while left <= right:
                mid = (left + right) >> 1
                val = events[mid][0]
                
                if val <= events[i][1]:
                    left = mid + 1
                else:
                    right = mid - 1
            # print(i ,left, sep="  ")        
            pick = events[i][2] + dp(left, k - 1) 
            not_picking = dp(i + 1, k)
            
            return max(pick, not_picking)
        
        return dp(0, k)
            
            