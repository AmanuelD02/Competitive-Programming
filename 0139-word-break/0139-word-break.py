class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root  = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for i in word:
            if i not in curr.nodes:
                curr.nodes[i] = TrieNode()
            curr = curr.nodes[i]
        curr.end = True
    
    
    def isPrefix(self, word):
        curr = self.root
        ends = []
        for i, char in enumerate(word):
            # print(i,char, word,curr.end)
            if char not in curr.nodes:
                return ends
            curr = curr.nodes[char]
            if curr.end == True:
                ends.append(i)

        return ends
    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        @lru_cache(None)
        def dp(i):
            # print(i,"start")
            if i == len(s):
                return True
            jump = False
            ends = trie.isPrefix(s[i:])
            # print("ends", ends)
            for end in ends:
                jump = jump or dp(i + end + 1)
            
            return jump
            
        return dp(0)    
            