from collections import defaultdict
class Node:
    def __init__(self):
        self.nodes = defaultdict()
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = Node()
            curr = curr.nodes[c]
        curr.end = True

    def search(self, word: str) -> bool:
        return self.helper(self.root, word)

    def helper(self, curr, word):
        for j, c in enumerate(word):
            if c =='.':
                for i in curr.nodes:
                    if self.helper(curr.nodes[i], word[j+1:] ):
                        return True
                return False
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return curr.end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)