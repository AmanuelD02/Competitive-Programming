class Solution:
    def countVowelPermutation(self, n: int) -> int:

        rules = {
            'a': ['e'],
            'e': ['a','i'],
            'i': ['a','e','o','u'],
            'o': ['i', 'u'],
            'u': ['a']
        }
        
        @cache
        def dp(i,letter):
            if i ==n:
                return 1
            
            count = 0
            for lett in rules[letter]:
                count += dp(i+1, lett)
            
            return count
        
        count = 0
        for letter in 'aeiou':
            count += dp(1,letter)
        
        return count %(10**9 + 7)