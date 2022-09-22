class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            cnt = ans = 0
            for n in nums:
                cnt += 1
                if n > bound:
                    cnt = 0
                ans += cnt
            return ans
        
        return count(right) - count(left-1)
    