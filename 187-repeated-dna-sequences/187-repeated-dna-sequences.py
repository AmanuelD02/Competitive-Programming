class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited, ans = set(), set()
        for i in range(len(s)-9):
            current = s[i: i + 10]
            if current in visited:
                ans.add(current)
            
            else:
                visited.add(current)
        
        return list(ans)