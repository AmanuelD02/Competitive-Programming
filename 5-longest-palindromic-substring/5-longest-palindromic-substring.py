class Solution:
    def longestPalindrome(self, s: str) -> str:
        N, longest = len(s), 0
        word = ""
        in_bound = lambda l, r: 0 <= l and r < N
        
        for i in range(len(s)):
            left = right = i
            while in_bound(left, right) and s[left] == s[right]:
                # print(left, right)
                if (right - left + 1) > longest:
                    word = s[left:right + 1]
                    longest = right - left + 1
                    # print("w",word)
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while in_bound(left, right) and s[left] == s[right]:
                if (right - left + 1) > longest:
                    word = s[left:right + 1]
                    longest = right - left + 1
                left -= 1
                right += 1
        # print(longest)
        return word            
            