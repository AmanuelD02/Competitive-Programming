class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.freq = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for w in word:
            if not w in curr.nodes:
                curr.nodes[w] = TrieNode()
            curr.nodes[w].freq += 1
            curr = curr.nodes[w]
    
    
    
    def count_prefix(self,word):
        total = 0
        curr = self.root
        for w in word:
            total += curr.nodes[w].freq
            curr = curr.nodes[w]
        
        return total
                
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.count_prefix(word))
        
        return ans
        