class Solution:
    def numIdenticalPairs(self, nums) -> int:
        def factorial(n):
            a = 0
            for i in range(1,n+1):
                a += i
            return a
        ans = [0] * 101
        
        for i in range(len(nums)):
            ans[nums[i]] +=1
        sol = 0
        print(ans)
        for i in range(len(ans)):
            if ans[i] != 0:
                temp = factorial(ans[i]-1)
                # print(i,temp)
                sol+=temp
        return sol
        