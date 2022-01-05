# https://leetcode.com/problems/predict-the-winner/
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) ==1:
            return True
        
        def recurs(start, end):
            if start == end:
                return nums[start]
            
            return max( nums[start] - recurs(start+1,end) ,  nums[end] - recurs(start, end-1)  )
        
        
        
        a = recurs(0, len(nums) -1 )
        return a >=0