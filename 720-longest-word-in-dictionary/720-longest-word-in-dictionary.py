class Node():
    def __init__(self):
        self.nodes = {}
        self.end  = False
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = Node()
            curr = curr.nodes[c]
        curr.end = True
        
    def search(self, word):
        if not len(word): return True
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return curr.end
        
            
class Solution:
    def longestWord(self, words: List[str]) -> str:
        output, trie = "", Trie()
        words.sort()
        for word in words:
            if trie.search(word[:-1]):
                trie.insert(word)
                output = word if len(word) > len(output) else output
        return output
        
        
        