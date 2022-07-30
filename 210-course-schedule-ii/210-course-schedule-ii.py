class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited, graph, backtrack = set(), defaultdict(list), set()
        
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        def dfs(node):
            visited.add(node)
            backtrack.add(node)
    
            for neigh in graph[node]:            
                if neigh in backtrack:
                    return False
                if neigh not in visited:
                    
                    valid = dfs(neigh)
                    if not valid: return False
            
            backtrack.remove(node)
            res.append(node)
            return True
        
        
        
        for i in range(numCourses):
            if i not in visited:
                valid = dfs(i)
                # print(i, valid)
                if not valid : return []
        
        return res[::-1]