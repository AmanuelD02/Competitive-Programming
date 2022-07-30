

from select import select


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
    
    def prefix(self, word1, word2):
        curr1 = self.root
        curr2 = self.root 
        counter = 0
        total = len(word1) + len(word2)


        for w1, w2 in zip(word1, word2):
            curr1 = curr1.nodes[w1]
            curr2 = curr2.nodes[w2]
            if curr1 != curr2:
                break
            
            
            
            
            counter += 1
                
        return total - (2 * counter)





    



s = input()

t = input()

s  = s[::-1]

t = t[::-1]

trie = Trie()
trie.insert(s)
trie.insert(t)

print(trie.prefix(s, t))


