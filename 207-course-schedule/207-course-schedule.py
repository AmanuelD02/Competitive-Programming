class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = 0
        graph, visited, backtrack = defaultdict(list), set(), set()
        
        # build the graph
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        def dfs(node):
            nonlocal count
            
            visited.add(node)
            backtrack.add(node)
            
            for neigh in graph[node]:
                if neigh in backtrack:
                    return False
                if neigh not in visited:
                    dfs(neigh)
            
            count += 1
            backtrack.remove(node)
        
        
        for i in range(numCourses):
            if i not in visited:
                dfs(i)
        
        return count == numCourses
            