class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_size = len(word1)
        w2_size = len(word2)
        
        @lru_cache(None)
        def dp(w1, w2):
            if w1 >= w1_size and w2 >= w2_size:
                return 0
            elif w1 >= w1_size:
                return w2_size - w2
            elif w2 >= w2_size:
                return w1_size - w1
            
            if word1[w1] == word2[w2]:
                return dp(w1 + 1, w2 + 1)
            
            insert_ops = 1 + dp(w1, w2 + 1)
            delete_ops = 1  + dp(w1 + 1, w2)
            replace_ops = 1 + dp(w1 + 1, w2 + 1)
            
            return min(insert_ops, delete_ops, replace_ops)
        
        return dp(0, 0)