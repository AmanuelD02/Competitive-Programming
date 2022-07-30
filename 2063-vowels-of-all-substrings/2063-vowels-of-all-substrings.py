class Solution:
    def countVowels(self, word: str) -> int:
        total, N = 0, len(word)
        for i, j in enumerate(word):
            if j in "aeiou":
                total += (i+1)*(N-i)
        
        return total