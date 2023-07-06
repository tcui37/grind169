import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) != 0 and len(max_heap) != 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x < y:
                x, y = y, x
            # x > y
            if y < x:
                heapq.heappush(max_heap, y - x)
        return -max_heap[0] if max_heap else 0
