class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(left,right, deleted):
            while left<= right:
                if s[left] == s[right]:
                    left +=1
                    right -=1
                    continue
                if deleted:
                    return False
                return isValid(left+1, right,True) or isValid(left, right-1, True)
            
            return True
        return isValid(0, len(s)-1, False)