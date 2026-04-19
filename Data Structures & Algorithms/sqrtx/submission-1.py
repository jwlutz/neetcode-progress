class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        res = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res
            
