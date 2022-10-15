class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph, incoming  = defaultdict(set), [0] * n
        for rich, poor in richer:
            graph[rich].add(poor)
            incoming[poor] += 1
        answer = list(range(n))
        queue = deque()
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
        
        
        while queue:
            rich = queue.popleft()
            for poor in graph[rich]:
                if quiet[answer[poor]] > quiet[answer[rich]]:
                    answer[poor] = answer[rich]
                incoming[poor] -= 1
                if incoming[poor] == 0:
                    
                    queue.append(poor)
        
        return answer
                
            