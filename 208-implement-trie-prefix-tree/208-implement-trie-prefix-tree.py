class Node:
    def __init__(self):
        self.all = [None]*26
        self.end = False
        

class Trie:

    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        cur = self.root
        for i,c in enumerate(word):
            if not cur.all[ord(c)- ord("a")]:
                cur.all[ord(c)- 97] = Node()
            cur = cur.all[ord(c)- ord("a")]
        cur.end = True
        
    def search(self, word: str, isPrefix = False ) -> bool:
        cur = self.root
        for i,c in enumerate(word):
            if cur.all[ord(c) - ord("a")]:
                cur = cur.all[ord(c) - 97]
                
            else:
                return False
        return cur.end or isPrefix

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)