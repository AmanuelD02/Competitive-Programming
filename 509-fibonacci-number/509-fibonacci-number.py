class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1 } 
        def recur(n):
            if memo.get(n) is not None:
                return memo[n]

            a = memo[n-1] = recur(n-1)
            b = memo[n-2] = recur(n-2)

            return  a + b
        return recur(n)
    
        