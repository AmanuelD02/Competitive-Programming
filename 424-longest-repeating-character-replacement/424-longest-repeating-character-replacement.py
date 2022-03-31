class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Max = 0 
        Global = 0
        freq = defaultdict(int)
        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            Max = max(Max, freq[s[right]])
            while Max + k <= right - left:
                freq[s[left]] -= 1
                Max = max(Max, freq[s[left]])
                left +=1
        
            Global = max(Global, right - left + 1)
        return Global