class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s2_freq = defaultdict(int)
        left = 0

        # print(s1_freq)
        for right, char in enumerate(s2):
            s2_freq[char] += 1

            
            while s2_freq[char] > s1_freq[char]:
                s2_freq[s2[left]] -= 1
                if s2_freq[s2[left]] == 0:
                    print(s2[left])
                    del s2_freq[s2[left]]
                left += 1
            if self.helper(s1_freq, s2_freq):
                return True
            # print(s2_freq)
        
        # print("\n\n")
        return False
    
    def helper(self, s1, s2):
        for key, val in s1.items():
            if s2[key] != val:
                return False
        return True