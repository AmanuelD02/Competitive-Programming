class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
        words.sort(key = lambda x: len(x), reverse = True)
        set_of_words = [set(x) for x in words]
        def helper(word1, j):
            for i in word1:
                if i in set_of_words[j]: return True
            return False
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not helper(words[i], j):
                    maximum = max(maximum, len(words[i]) * len(words[j]))
                    break
        return maximum
    
                
            
        