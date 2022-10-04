class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:        
        arr.append(float("-inf"))
        ans, stack, MOD = 0, [], (10**9) + 7
        
        for i,num in enumerate(arr):
            if stack:
                while stack and arr[stack[-1]] > num:
                    cur = stack.pop()
                    left = stack[-1] if stack else -1
                    ans += arr[cur] * (i-cur) * (cur-left)
            stack.append(i)
        
        return ans % MOD
            