class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[tuple(sorted(word))].append(word)
        
        answer = []
        for key, val in anagrams.items():
            answer.append(val)
        
        return answer
            