class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq = defaultdict(int)
        for word in words2:
            count = Counter(word)
            for letter, val in count.items():
                freq[letter] = max(freq[letter], val)
        ans = []
        for word in words1:
            count = Counter(word)
            for letter, val in freq.items():
                if freq[letter] > count[letter]:
                    break
            else:
                ans.append(word)
                
            
        return ans
                
                