class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        left, right = 1, max(time) * totalTrips
        best = right
        while left <= right:
            mid = left + (right - left) //2
            if self.canFinish(time, mid, totalTrips):
                best = min(best, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return best

    
    
    def canFinish(self, time, curTime, totalTrips):
        total = 0
        for t in time:
            total += curTime // t
        
        return total >= totalTrips
    