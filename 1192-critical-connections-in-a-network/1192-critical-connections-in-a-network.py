class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        discovery_time = defaultdict(int)
        lowest_discovery_time = defaultdict(int)
        visited = set()
        time = 0
        graph = defaultdict(list)
        critical_conn = []
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent = -1):
            nonlocal time
            time += 1
            discovery_time[node] = lowest_discovery_time[node] = time
            visited.add(node)
            
            for neigh in graph[node]:
                if neigh != parent:
                    if neigh in visited:
                        lowest_discovery_time[node] = min(lowest_discovery_time[node], discovery_time[neigh])
                    else:
                        dfs(neigh, node)
                        lowest_discovery_time[node] = min(lowest_discovery_time[node], lowest_discovery_time[neigh])

                    if discovery_time[node] < lowest_discovery_time[neigh]:
                        critical_conn.append([node, neigh])
                    
        dfs(0)
        return critical_conn
            