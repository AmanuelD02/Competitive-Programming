class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        visited = defaultdict(int)
        running_sum = 0
        ans = 0
        visited[0] = 1
        for num in nums:
            running_sum += num
            ans += visited[running_sum - goal]
            visited[running_sum] += 1
        
        return ans