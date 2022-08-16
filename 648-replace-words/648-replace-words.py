class Node:
    def __init__(self):
        self.node = [None] * 26
        self.end = False
class Trie:

    def __init__(self):
        self.root = Node()
        
        
    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            idx = ord(char) - ord('a')
            if curr.node[idx] == None:
                 curr.node[idx] = Node()
            curr =  curr.node[idx]
            
        curr.end = True

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass
    def shortestPrefix(self, word) -> str:
        curr = self.root
        for i,char in enumerate(word):
            index = ord(char) - ord('a')
            if not curr.node[index]:
                return word
            
            if curr.node[index].end:
                return word[:i+1]
            curr = curr.node[index]
        
        return word
        
            
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        sentence = sentence.split()
        ans = []
        for word in sentence:
            ans.append(trie.shortestPrefix(word))
        
        
        return " ".join(ans)
    
        