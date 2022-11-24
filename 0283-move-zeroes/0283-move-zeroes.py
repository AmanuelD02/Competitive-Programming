class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = deque()
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
            elif len(zeros) >= 1:
                cur = zeros.popleft()
                nums[cur], nums[i] = nums[i], nums[cur]
                zeros.append(i)
        