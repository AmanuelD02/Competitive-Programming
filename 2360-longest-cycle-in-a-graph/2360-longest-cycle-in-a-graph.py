class Solution:

    def longestCycle(self, edges: List[int]) -> int:

            visited = set()
            longest_cycle = target = -1

            def dfs(node):
                nonlocal target, longest_cycle
                if node in visited:
                    target = node
                    return 0

                visited.add(node)
                if edges[node] == -1:
                    return 0
                cur_cycle = 1 + dfs(edges[node])

                if node == target:
                    target = -1
                    longest_cycle = max(longest_cycle, cur_cycle)

                return cur_cycle


            for node in range(0, len(edges)):
                if node not in visited:
                    dfs(node)

            return longest_cycle