class Solution:
    def checkPartitioning(self, s: str) -> bool:
        s_size = len(s)
        
        @cache
        def isPal(left, right):
            if left == right:
                return True
            if s[left] != s[right]:
                return False
            if left + 1 == right:
                return True
            return isPal(left + 1, right - 1)


        
        
        for i in range(s_size - 2):
            if not isPal(0, i): continue
            for j in range(i+1 ,s_size - 1):
                if isPal(i+1, j) and isPal(j+1, s_size - 1):
                    return True
        
        return False
        
        
            