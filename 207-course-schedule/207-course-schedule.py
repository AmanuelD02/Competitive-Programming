class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: return True
        
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        for course, pre in prerequisites:
            graph[pre].add(course)
            in_degree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        
        course = 0
        while queue:
            c = queue.popleft()
            course += 1
            for neigh in graph[c]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)
        
        return course == numCourses
                
        
            