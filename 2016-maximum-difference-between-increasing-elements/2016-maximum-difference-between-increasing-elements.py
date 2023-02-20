class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx = 0
        
        heap = [nums[0]]
        for num in nums[1:]:
            maxx = max(maxx, num - heap[0])
            heappush(heap, num)
        
        return maxx if maxx > 0 else -1 