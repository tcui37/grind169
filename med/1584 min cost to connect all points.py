import heapq
import math


class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, node: int) -> int:
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def join(self, node1: int, node2: int) -> bool:
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return False

        if self.rank[root1] == self.rank[root2]:
            self.rank[root1] += 1
            self.root[root2] = root1
        elif self.rank[root1] > self.rank[root2]:
            self.root[root2] = self.root[root1]
        else:
            self.root[root1] = self.root[root2]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskals
        # n = len(points)
        # if len(points) <= 1: return 0
        # def dist(p1:list[int],p2:list[int]):
        #     return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        # edges = []
        # for i in range(len(points)):
        #     for j in range(i+1,len(points)):
        #         pi,pj = points[i],points[j]
        #         edges.append((dist(pi,pj),i,j))
        # edges.sort(key=lambda x: x[0])
        # total = 0
        # ufind = UnionFind(n)
        # used = 0
        # for w,i,j in edges:
        #     if ufind.join(i,j):
        #         print(w,i,j)
        #         total += w
        #         used +=1
        #         if used == n-1:
        #             break

        # return total

        # prims
        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        n = len(points)
        heap = [(0, 0)]
        in_mst = [False] * n
        c = 0
        edges = 0

        while edges < n:
            w, i = heapq.heappop(heap)
            if in_mst[i]:
                continue
            in_mst[i] = True
            edges += 1
            c += w
            for j in range(n):
                if not in_mst[j]:
                    heapq.heappush(heap, (dist(i, j), j))
        return c
