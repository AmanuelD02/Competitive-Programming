class Solution:
    def countSubstrings(self, s: str) -> int:
        @lru_cache(None)
        def isPalindrome(left, right):
            if left >= right:
                return True
            if s[left] == s[right]:
                return isPalindrome(left + 1, right -1)
            return False
        
        
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    count += 1
        
        return count