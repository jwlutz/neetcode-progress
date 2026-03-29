class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][-1] < target:
                lo = mid + 1
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                if matrix[mid][0] == target:
                    return True
                lo2, hi2 = 0, len(matrix[mid]) - 1
                while lo2 <= hi2:
                    mid2 = (lo2 + hi2) // 2
                    if matrix[mid][mid2] < target:
                        lo2 = mid2 + 1
                    elif matrix[mid][mid2] > target:
                        hi2 = mid2 - 1
                    else:
                        return True
                return False
        return False