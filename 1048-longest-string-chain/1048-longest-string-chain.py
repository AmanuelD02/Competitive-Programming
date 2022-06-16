class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)
        
        @cache
        def dp(word):
            longest = 1
            for i in range(len(word)):
                newWord = word[:i] + word[i+1:]
                
                if newWord in words:
                    longest =max(1 + dp(newWord), longest)
            return longest
        
        longest = 0
        for word in words:
            longest = max(longest, dp(word))
        return longest
        
        
        