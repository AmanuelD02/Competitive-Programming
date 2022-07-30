class Node:
    def __init__(self):
        self.nodes = [None] * 26
        self.end = 0

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for i in word:
            diff = ord(i) - ord('a')
            if not curr.nodes[diff]:
                curr.nodes[diff] = Node()
            curr = curr.nodes[diff]
        curr.end += 1
        
    def search(self, word):
        curr = self.root
        for i in word:
            diff = ord(i) - ord('a')
            if not curr.nodes[diff]:
                return False
            curr = curr.nodes[diff]
        return curr.end
        

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap, trie = [], Trie()
        for word in words:
            trie.insert(word)
        for word in set(words):
            freq = trie.search(word)
            
            heappush(heap, (-freq, word))
        
        ans = []
        # print(heap)
        while heap and k >0:
            word = heappop(heap)[1]
            ans.append(word)
            k-=1
        return ans
        
            
        