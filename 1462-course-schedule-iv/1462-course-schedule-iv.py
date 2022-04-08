class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph, visited =  defaultdict(set), set()
        lej = defaultdict(set)
        
        for pre, course  in prerequisites:
            graph[pre].add(course)
           
        def dfs(node):
            visited.add(node)
            
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
                lej[node].add(neigh)
                lej[node].update( lej[neigh])
        
        for i in range(numCourses):
            if i not in visited:
                dfs(i)
        
        ans = []
        for pre, course in queries:
            if course in lej[pre]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans