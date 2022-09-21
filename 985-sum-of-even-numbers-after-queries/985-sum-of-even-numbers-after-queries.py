class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumOfTotals = sum([x for x in nums if x%2==0])
        ans = []
        for val, indx in queries:
            if (nums[indx] %2 == 0) and (nums[indx] + val) %2 ==0:
                sumOfTotals += val
            elif (nums[indx] %2 == 1) and (nums[indx] + val) %2 ==0:
                sumOfTotals += nums[indx] + val
            elif (nums[indx] %2 == 0) and (nums[indx] + val) %2 ==1:
                sumOfTotals -= nums[indx]
                
            ans.append(sumOfTotals)
            
            nums[indx] += val
            # print(ans, nums)
        
        return ans
                