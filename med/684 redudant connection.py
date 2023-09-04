class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for a, b in edges:
            n = max(n, a, b)

        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n + 1)]
                self.size = [1 for i in range(n + 1)]

            def root(self, node):
                while node != self.parent[node]:
                    node = self.parent[node]
                return node

            def merge(self, node1, node2):
                root1 = self.root(node1)
                root2 = self.root(node2)
                if root1 == root2:
                    return [node1, node2]

                if self.size[root1] == self.size[root2]:
                    self.parent[root2] = root1
                    self.size[root1] += 1
                elif self.size[root1] > self.size[root2]:
                    self.parent[root2] = root1
                else:
                    self.parent[root1] = root2
                return None

        ufind = UnionFind(n)

        for a, b in edges:
            l = ufind.merge(a, b)
            if l:
                return l
