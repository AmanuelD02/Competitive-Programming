class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        

        removed = 0
        interval = intervals[0]
        for i in range(1, len(intervals)):
            curInterval = intervals[i]
            if curInterval[0] >= interval[1] or curInterval[1] <= interval[0]:
                interval = curInterval
            elif interval[1] > curInterval[1]:
                interval = curInterval
                removed += 1
            else:
                removed += 1
                
        
        
        return removed
            