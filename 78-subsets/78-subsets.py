class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = 2**len(nums)
        for i in range(N):
            picked = []
            index = 0
            while i:
                if i & 1:
                    picked.append(nums[index])
                i = i >> 1
                index += 1
            res.append(picked)
        return res