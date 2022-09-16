class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        elements_in_subarray = defaultdict(int)
        minHeap, maxHeap = [], []
        maxSubArray = left= right = 0
        
        while right < len(nums):
            elements_in_subarray[nums[right]] += 1
            heappush(minHeap, nums[right])
            heappush(maxHeap, -nums[right])
            
            minElement, maxElement = minHeap[0], -maxHeap[0]            
            
            while abs(minElement - maxElement) > limit:
                elements_in_subarray[nums[left]] -= 1
                minElement, maxElement = minHeap[0], -maxHeap[0]
                while elements_in_subarray[minElement] <= 0:
                    heappop(minHeap)
                    minElement = minHeap[0]
                while elements_in_subarray[maxElement] <= 0:
                    heappop(maxHeap)
                    maxElement = -maxHeap[0]
                left += 1
                
            maxSubArray = max(maxSubArray, right - left + 1)
            right +=1
        return maxSubArray 
            
                
        
        