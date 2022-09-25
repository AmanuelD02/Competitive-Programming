class TrieNode():
    def __init__(self):
        self.nodes = [0, 0]
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (num>>i) & 1
            if not curr.nodes[bit]:
                curr.nodes[bit] = TrieNode()
            curr = curr.nodes[bit]
            
    def max_xor(self, num):
        xor = 0
        curr = self.root
        for i in range(31, -1, -1):
            bit = (num>>i) & 1
            if curr.nodes[1 - bit]:
                xor |= 1<<i
                curr = curr.nodes[1- bit]
            else:
                curr = curr.nodes[bit]
        return xor
    
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        
        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, trie.max_xor(num) )
        
        return max_xor