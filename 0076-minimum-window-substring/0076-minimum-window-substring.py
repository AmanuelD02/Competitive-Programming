class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        left = right = 0
        target = Counter(t)
        size_s = len(s)
        current_freq = defaultdict(int)
        
        minimum_window_size = float("inf")
        minimum_window_string =  ""

        while right < size_s:
            if s[right] in target:
                current_freq[s[right]] += 1
            while self.compareSubString(current_freq, target):
                if right - left + 1 < minimum_window_size:
                    minimum_window_size = right - left + 1
                    minimum_window_string = s[left: right + 1]
                if target[s[left]]:
                    current_freq[s[left]] -= 1
                    if current_freq[s[left]] == 0:
                        del current_freq[s[left]]
                left += 1
            
            right += 1
        
        
        return minimum_window_string
                    
    def compareSubString(self, subString, target):
        for key, val in target.items():
            if subString[key] < val:
                return False
        return True
                
            