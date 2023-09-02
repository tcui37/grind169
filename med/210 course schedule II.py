class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for after, before in prerequisites:
            adj[before].append(after)

        def dfs(node, adj, seen, order, finished):
            for neighbor in adj[node]:
                if neighbor in seen and neighbor not in finished:
                    return None
                elif neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor, adj, seen, order, finished) is None:
                        return None
            finished.add(node)
            order.append(node)
            return order

        seen, order, finished = set(), [], set()
        for c in range(numCourses):
            if c not in seen:
                seen.add(c)
                if dfs(c, adj, seen, order, finished) == None:
                    return []
        order.reverse()
        return order
