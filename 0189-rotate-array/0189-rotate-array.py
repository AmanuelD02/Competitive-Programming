class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if k == n or k == 0:
            return
        k = k % n
        k = n - k -1

        nums[k+1:], nums[:k + 1] = nums[:k + 1], nums[k+1:]