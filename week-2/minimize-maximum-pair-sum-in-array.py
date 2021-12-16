class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        Max = 0
        left =0
        right = len(nums) -1
        while(right> left):
            Max = max(nums[right]+ nums[left], Max)
            right-=1
            left +=1
        return Max
            
            
        