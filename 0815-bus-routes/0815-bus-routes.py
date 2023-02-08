class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        N = len(routes)
        
        RMap = defaultdict(set)
        BMap = defaultdict(set)
        
        for i in range(N):
            for bus in routes[i]:
                RMap[i].add(bus)
                BMap[bus].add(i)                        
        
        queue = deque(BMap[source])
        steps = 1
        
        bus_visited = set()
        route_visited = set(BMap[source])
        
        
        while queue:                                                          
            
            for _ in range(len(queue)):
                current_route= queue.popleft()
                
                for bus in RMap[current_route]:
                    if bus not in bus_visited:
                        bus_visited.add(bus)
                        
                        if bus == target:
                            return steps
                        
                        for route in BMap[bus]:
                            if route not in route_visited:
                                route_visited.add(route)
                                queue.append(route)
            
            steps += 1
        
        return -1