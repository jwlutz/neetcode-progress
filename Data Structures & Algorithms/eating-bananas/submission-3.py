class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        result = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            counter = 0
            for pile in piles:
                counter += math.ceil(pile / mid)
            if counter <= h:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return result