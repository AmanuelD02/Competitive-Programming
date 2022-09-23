class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        prefixSum = [0] * (N+1)
        for start, end, direction in shifts:
            d= -1 if direction == 0 else 1
            prefixSum[start] += d
            prefixSum[end + 1] -= d
        for i in range(1,N):
            prefixSum[i] += prefixSum[i-1]
        for i in range(N):
            final = (ord(s[i])  + prefixSum[i] - 97) % 26
            prefixSum[i] = chr(final + 97)
        return "".join(prefixSum[:-1])
