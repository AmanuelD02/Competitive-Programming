class Node:
    def __init__(self):
        self.nodes = {}
        self.end = False
        
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

    def search(self, start, word, count):
        curr = start
        for i in word:

    
    def prefix(self, word1, word2):
        curr1 = self.root
        curr2 = self.root 
        counter = 0
        total = len(word1) + len(word2)


        for w1, w2 in zip(word1, word2):
            curr1 = curr1.nodes[w1]
            curr2 = curr2.nodes[w2]
            if curr1 != curr2:
                return total - 2*counter
            
            
            
            
            counter += 1
                
        return total - 2*counter



trie = Trie()
n, m  = list(map(int, input().split()))
for i in range(n):
    trie.insert(input())


for j in range(m):
    word = input()

