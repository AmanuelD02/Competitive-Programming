class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        visited = set()
        groups = 0
        
        
        for word in strs:
            if word not in visited:
                self.dfs(word, visited, strs)
            
                groups += 1
        
        return groups
        
        
    def dfs(self, word, visited, strs):
        visited.add(word)
        for nextWord in strs:
            if nextWord not in visited and self.isSimilar(word, nextWord) :
                self.dfs(nextWord, visited, strs)
            
            
    
    def isSimilar(self, word1, word2):
        diff = 0
        for i, j in zip(word1, word2):
            if i != j:
                diff += 1
        
        
        return diff == 0 or diff == 2