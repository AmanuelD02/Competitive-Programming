class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        days.sort()
        
        @cache
        def dp(i):
            if i >= N:
                return 0
            one_next = bisect.bisect_left(days, days[i] + 1)
            seven_next = bisect.bisect_left(days, days[i] +  7 )
            month_next = bisect.bisect_left(days, days[i] +  30 )
            
            one  = costs[0] + dp(one_next)
            seven = costs[1] + dp(seven_next)
            month =  costs[2] + dp(month_next)
            
            return min(one, seven, month)
        
        return dp(0)
            