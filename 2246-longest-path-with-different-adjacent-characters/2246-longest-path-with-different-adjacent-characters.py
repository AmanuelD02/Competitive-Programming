class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(set)

        for i, num in enumerate(parent):
            graph[num].add(i)
        
        res = 1
        
        def dfs(node):
            nonlocal res
            longest, subtree = 1, []

            for neigh in graph[node]:
                if s[node] == s[neigh]:
                    dfs(neigh)
                
                else:
                    subtree.append(dfs(neigh))
            
            subtree.sort(reverse = True)
            if subtree:
                res = max(res, 1 + sum(subtree[:2]))
            
                longest = 1 + subtree[0]
            
            return longest
        
        dfs(graph[-1].pop())
        return res
  