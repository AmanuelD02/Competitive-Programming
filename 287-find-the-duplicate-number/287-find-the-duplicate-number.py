class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) -1
        
        def counter(n):
            c = 0
            for i in nums:
                if i <= n:
                    c += 1
            return c
        while low <= high:
            mid =( low + high) //2
            val = counter(mid)
            if val > mid:
                duplicate = mid
                high = mid -1
            else:
                low = mid + 1
        return duplicate
            
        