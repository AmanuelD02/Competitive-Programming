class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(largest):
            subarray = 1
            count = 0
            for n in nums:
                count += n
                if count > largest:
                    subarray += 1
                    count = n
            return subarray <= m
        
        
        left, right = max(nums), sum(nums)
        res = right
        while left <= right:
            mid = left + (right - left) //2
            if canSplit(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res