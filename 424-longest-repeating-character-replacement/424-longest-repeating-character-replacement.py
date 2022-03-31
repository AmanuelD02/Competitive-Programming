class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Global = left = Max = 0 
        freq = defaultdict(int)
        
        for right in range(len(s)):
            freq[s[right]] += 1
            Max = max(Max, freq[s[right]])
            
            while Max + k <= right - left:
                freq[s[left]] -= 1
                Max = max(Max, freq[s[left]])
                left +=1
        
            Global = max(Global, right - left + 1)
            
        return Global