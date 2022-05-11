class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        TWENTY_FOUR = 24*60
        difference = float("inf")
        N = len(timePoints)
        def calculate_time_difference(time1, time2):
            time1 = int(time1[:2]) * 60 + int(time1[3:])
            time2 = int(time2[:2]) * 60 + int(time2[3:])
            return min(abs(time1 - time2), TWENTY_FOUR - abs(time1 - time2))
        
        for i in range(N):
            # print(difference)
            difference = min(difference, calculate_time_difference(timePoints[i], timePoints[(i+1)%N] ))
        return difference
            