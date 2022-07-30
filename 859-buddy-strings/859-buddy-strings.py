class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or len(s) == 1:
            return False
        
        if s == goal:
            visited = set()
            for c in s:
                if c in visited: return True
                visited.add(c)
            return False
        
        pairs = []
        for a, b in zip(s, goal):
            if a!=b:
                pairs.append((a,b))
            if len(pairs) > 2:
                return False
        
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]