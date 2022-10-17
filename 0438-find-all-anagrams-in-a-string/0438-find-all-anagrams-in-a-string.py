from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        subString, target = Counter(), Counter(p)
        anagrams = []
        for i in range(len(s)):
            subString[s[i]] += 1
            if i - len(p) + 1 > 0:
                subString[s[i - len(p)]] -= 1
                if subString[s[i - len(p)]]  == 0:
                    del subString[s[i - len(p) ]] 
            if target == subString:
                anagrams.append(i - len(p) + 1)
        
        return anagrams
            
            
        
            