class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        
        for counter in range(len(words[0])):
            for word in words:
                if counter < len(word) and word[counter] == words[0][counter]:
                    continue
                
                return word[:counter]
        return words[0]
