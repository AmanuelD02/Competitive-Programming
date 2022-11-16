class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        search = word
        count = 0
        while sequence.find(search) != -1:
            count += 1
            search += word
        
        return count