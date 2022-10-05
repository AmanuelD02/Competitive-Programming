class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix = [1], [1]
        N = len(nums)
        countL = countR = maxNum = maxLen =  0
        
        for i in range(len(nums)):
            j = N - 1 - i
            prevSum = prefix[-1] if prefix[-1] != 0 else 1
            prefix.append(nums[i] * prevSum)

            sufSum = suffix[-1] if suffix[-1] != 0 else 1
            suffix.append(nums[j]* sufSum)
          
        
        # print(prefix[1:])
        # print(suffix[1:])
        return max(*suffix[1:],*prefix[1:])
        # print(max(suffix))
                           
                           
            