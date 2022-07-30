class Solution:
    def countPrimes(self, N: int) -> int:
        nums = [0] * N
        # 0 for marked
        # -1 for unmarked
        count = 0
        for i in range(2, len(nums)):
            temp = 2
            if nums[i] == 0:
                count += 1
                while i * temp < N:
                    nums[i * temp] = -1
                    temp += 1
        
        return count