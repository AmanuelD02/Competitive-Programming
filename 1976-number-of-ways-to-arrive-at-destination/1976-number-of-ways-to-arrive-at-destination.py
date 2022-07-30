class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dest, time in roads:
            graph[src].append((dest, time))
            graph[dest].append((src, time))
        
        heap = [(0,0)]
        shortest_dist = [float("inf")] * n
        no_ways = [0] *n
        no_ways[0] = 1
        shortest_dist[0] = 0
        
        while heap:
            old_time, node = heappop(heap)
            if old_time > shortest_dist[node]: continue
                
            for neigh, cur_time in graph[node]:
                new_time = old_time + cur_time
     
                if new_time == shortest_dist[neigh]:
                    no_ways[neigh] += no_ways[node]
                elif new_time < shortest_dist[neigh]:
                    no_ways[neigh] = no_ways[node]
                    shortest_dist[neigh] = new_time
                    heappush(heap, (new_time, neigh))
        
        return no_ways[-1]  % 1_000_000_007
        