class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if sequence == word:
            return 1
        count = idx = 0
        N, M  = len(word), len(sequence)
        max_rep = 0
        for idx in range(M - N + 1):
            while idx <= M - N :
                if sequence[idx: idx + N] == word:
                    count += 1
                    idx += N
                    max_rep = max(max_rep, count)
                else:
                    idx += 1
                    count = 0
            count = 0
        
        return max_rep
        