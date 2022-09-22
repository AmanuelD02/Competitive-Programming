class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def check(s,w):
            s1, s2, w1, w2, S,W = 0,0,0,0, len(s), len(w)
            
            while s1 < S and w1 < W:
                if s[s1] != w[w1]: return False
                
                while s2 < S and s[s1] ==s[s2]: s2+=1
                while w2 < W and w[w1] ==w[w2]: w2+=1
                if s2 - s1 != w2 - w1 and s2 - s1 < max(3, w2 - w1): return False
                
                s1,w1 = s2, w2
            
            return s1 == S and w1 == W
        
        count = 0
        for word in words:
            count += int(check(s,word))
        return count