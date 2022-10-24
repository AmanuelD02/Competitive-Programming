class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def countPairs(n):
            N = len(nums)
            left = ans = 0
            for right in range(1, N):
                while left <= right and nums[right] - nums[left] > n:
                    left += 1
                ans += (right - left)
                
            return ans
        
        left = float("inf")
        for i in range(len(nums) -1):
            left = min(left, nums[i+1] - nums[i])
        
        right = nums[-1] - nums[0]
        # print(left, right)
        while left <= right:
            mid = (left +  right) //2
            # print(mid, countPairs(mid))
            if countPairs(mid) >= k:
                right = mid - 1
            else:
                left = mid + 1
        
        return left