class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            result = target - num
            if result in store:
                return [store[result], i]
            else:
                store[num] = i
                