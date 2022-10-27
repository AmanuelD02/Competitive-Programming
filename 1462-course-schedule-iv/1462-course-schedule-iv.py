class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[False]*(numCourses) for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x][y] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
        
    
        return [ graph[x][y] for x,y in queries]
                               
        