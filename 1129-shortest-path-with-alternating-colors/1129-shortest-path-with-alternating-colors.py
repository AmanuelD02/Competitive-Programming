class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        # Build the graph
        graphs = [defaultdict(set), defaultdict(set)]
        for a, b in redEdges:
            graphs[0][a].add(b)
        for a, b in blueEdges:
            graphs[1][a].add(b)
        
        shortestDist = [float("inf")] * n
        queue = deque([(0,1), (0,0)])
        level = -1
        while queue:
            level +=1
            for i in range(len(queue)):
                node, color = queue.popleft()
                shortestDist[node] = min(shortestDist[node], level)
                neighs = graphs[1 - color][node]
                for n in neighs:
                    queue.append((n,1 - color))
                graphs[1- color][node] = set()
        for i in range(len(shortestDist)):
            if shortestDist[i] == float("inf"):
                shortestDist[i] = -1
        return shortestDist