class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            x = -(heapq.heappop(neg_stones))
            y = -(heapq.heappop(neg_stones))
            if x < y:
                heapq.heappush(neg_stones, -(y - x))
            elif x == y:
                if not neg_stones:
                    return 0
                continue
            else:
                heapq.heappush(neg_stones, -(x - y))

        return -neg_stones[0] if neg_stones else 0
            