class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        size_s = len(s)
        resIndx, resLen = [1,0], float("inf")
        target, window = {}, {}
        
        for c in t:
            target[c] = 1 + target.get(c, 0)
        
        need, have, left = len(target), 0, 0
        for right in range(size_s):
            window[s[right]] = 1 + window.get(s[right], 0)
            if s[right] in target and window[s[right]] == target[s[right]]:
                have += 1
            
            while have == need:
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    resIndx = [left, right + 1]
                    
                window[s[left]] -= 1 
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1
        
        l, r = resIndx 
        
        return s[l: r]
            
                
            