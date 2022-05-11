class Solution:
    def countVowelStrings(self, n: int) -> int:
        result = [1]*5
        for i in range(n):
            for j in range(3,-1,-1):
                result[j] = result[j] + result[j+1]
        
        return result[0]
            