class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        left, right = min(nums), max(nums)
        best = right
        while left <= right:
            mid = (left + right) // 2
            # print(mid, self.canMinimize(nums[:], mid))
            if self.canMinimize(nums[:], mid):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        
        return best
            
    
    
    
    
    def canMinimize(self, nums, target):
        for i in range(1, len(nums)):

            k = target - nums[i -1]
            if k < 0 or nums[i] - k > target:
                # print(k, i, nums)
                return False
            nums[i] -= k

        
        return True