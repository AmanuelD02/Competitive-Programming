class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph, incoming = defaultdict(set), [0] * n
        
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            incoming[a] += 1
            incoming[b] += 1
        
        queue = deque()
        for i in range(n):
            if incoming[i] ==1:
                queue.append(i)
        
        answer = [0]
        visited = set()
        while queue:
            answer = queue.copy()
            for i in range(len(queue)):
                curr = queue.popleft()
                for neigh in graph[curr]:
                    incoming[neigh] -= 1
                    if incoming[neigh] == 1:
                        queue.append(neigh)
        
        return answer
                    
        