class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0,1,1]
        if n <= 2:
            return ans[n]
       
        for i in range(n-2):
            ans.append(ans[-1] + ans[-2] + ans[-3])
        
        return ans[-1]

        
        
        