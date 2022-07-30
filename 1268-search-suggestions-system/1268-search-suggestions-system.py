class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.suggestion = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    
    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.nodes:
                curr.nodes[w] = TrieNode()
                
            curr = curr.nodes[w]
            curr.suggestion.append(word)
            curr.suggestion.sort()
            if len(curr.suggestion) >3:
                curr.suggestion.pop()
        
    
    def search(self, word):
        curr = self.root
        ans = []
        for w in word:
            if not w in curr.nodes:
                ans.append([])
                curr.nodes = {}
                continue
            ans.append(curr.nodes[w].suggestion)
            curr = curr.nodes[w]
        return ans
    
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in sorted(products):
            trie.insert(product)
        return trie.search(searchWord)