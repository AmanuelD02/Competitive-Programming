class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(-math.inf)
        N = len(arr)
        stack = [-1]
        numSub  = [1] * N
        
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                cur = stack.pop()
                numSub[cur] = max(1, cur - stack[-1]) * max(1, i - cur)
            stack.append(i)
        
        totalSum = 0
        for i in range(N - 1):
            totalSum += numSub[i] * arr[i]
        
        return totalSum % ((10**9) + 7)
        
        