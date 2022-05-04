class Node:
    def __init__(self):
        self.nodes = {}
        self.end = False
        self.index = None
        
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
    def search(self, word, s):
        curr = self.root
        indx = 0
        for i in range(len(word)):
            c = word[i]
            if curr.nodes[c].index == None:
                curr.nodes[c].index = -1
                for j in range(indx, len(s)):
                    if c == s[j]:
                        curr.nodes[c].index = j
                        indx = j + 1
                        break
            if curr.nodes[c].index < 0:
                return False
            indx = curr.nodes[c].index + 1
            curr = curr.nodes[c]
        return True
    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie, output = Trie(), 0
        words.sort()
        for word in words:
            trie.insert(word)
        
        for word in words:
            output += trie.search(word, s)
            
        return output
        