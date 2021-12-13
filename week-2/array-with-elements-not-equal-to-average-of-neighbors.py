# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        lst = []
        left = 0
        right = len(nums) -1
        while(left<right):
            lst.append(nums[right])
            lst.append(nums[left])
            right -=1
            left += 1
        if left ==right:
            lst.append(nums[left])
        # print(lst)
        return lst