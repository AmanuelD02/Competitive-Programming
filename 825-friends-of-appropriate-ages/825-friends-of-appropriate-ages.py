class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        for i in range(1, 121):
            count[i] += count[i-1]
        
        total = 0
        for age in ages:
            lb = math.floor(age/2) + 7
            total += max(0,count[age] - count[lb]-1)
        return total
            
        