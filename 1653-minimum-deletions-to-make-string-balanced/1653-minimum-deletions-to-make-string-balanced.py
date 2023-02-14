class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        A = [0] * (N + 1)
        B = [0] * (N  + 1)
        
        for i in range(N):
            j = N - i - 1
            B[i] = B[i - 1]
            A[j] = A[min(j + 1, N - 1)]

            if s[j] == 'a':
                A[j] += 1
            
            if s[i] == 'b':
                B[i] += 1

        ans = float("inf")
        for i in range(N + 1):
            ans = min(ans, A[i] + B[i - 1])
        
        return ans