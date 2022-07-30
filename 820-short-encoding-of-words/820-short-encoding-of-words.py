class TrieNode:
    def __init__(self):
        self.nodes = {}
class Trie:
    def __init__(self):
        self.root =TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = TrieNode()
            curr = curr.nodes[c]
    
    def isPrefix(self, word):
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return True
    

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for i in range(len(words)):
            words[i] = words[i][::-1]
            
        words = sorted(words, key = lambda x: len(x), reverse = True)
        ans = 0
        for word in words:
            if not trie.isPrefix(word):
                trie.insert(word)
                ans += len(word) + 1
        return ans
