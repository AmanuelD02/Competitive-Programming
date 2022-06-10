class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        words = set()
        longest = left = right = 0
        while right < len(s):
            if s[right] in words:
                longest = max(longest, right - left)
                while s[right] in words:
                    words.remove(s[left])
                    left += 1
            words.add(s[right])
            right += 1
        longest = max(longest, right - left)
        
        return longest
                
        