class Solution:
    def countPrimes(self, N: int) -> int:
        if N <2: return 0
        nums = [1] * N
        # 0 for marked
        # -1 for unmarked
        count = 0
        i = 2
        while i*i < N:
            # print(i , nums[i])
            if nums[i]:
                count += 1
                j = i*i
                while j < N:
                    # print(j)
                    nums[j] = 0
                    j += i
            i += 1
        
        return sum(nums) - 2