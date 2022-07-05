class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        longest = 0
        for i in all_nums:
            if i-1 not in all_nums:
                counter =1
                j=i
                while(j+1 in all_nums):
                    counter+=1
                    j+=1
                    
                longest = max(longest,counter)
            
        return longest