import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = {}
        k = groupSize
        for num in hand:
            counts[num] = counts.get(num, 0) + 1

        pq = hand
        heapq.heapify(pq)

        while counts:
            min_num = pq[0]
            for i in range(min_num, min_num + k):
                if i not in counts:
                    return False
                counts[i] = counts[i] - 1
                if counts[i] <= 0:
                    del counts[i]
            while pq and pq[0] not in counts:
                heapq.heappop(pq)
        return True
