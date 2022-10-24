class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        if k == 25:
            return len(s)
    
        max_subsequence = defaultdict(int)
        for char in s:
            cur = ord(char) - ord('a')
            longest = -1
            
            for i in range(cur - k, cur + k + 1):
                if 0<= i <= 25:
                    longest = max(longest, 1 + max_subsequence[chr(i + ord('a'))])
                    
            max_subsequence[char] = max(max_subsequence[char] , longest)
       
        
        return max(max_subsequence.values())