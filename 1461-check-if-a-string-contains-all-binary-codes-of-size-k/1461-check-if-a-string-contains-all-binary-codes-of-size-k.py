class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_comb = set()
        for i in range(len(s)-k+1):
            all_comb.add(s[i:i + k])
            # print(s[i:k])
        # print(all_comb)
        return len(all_comb) == 2**k
    
            
            