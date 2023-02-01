class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = res = len(blocks)
        prefix = [0] * N
        
        for i, block in enumerate(blocks):
            prefix[i] = prefix[i - 1] + int(block == 'W')
        
        prefix.append(0)

        for i in range(N - k + 1):
            res = min(res, prefix[i + k - 1] - prefix[i - 1])

        return res