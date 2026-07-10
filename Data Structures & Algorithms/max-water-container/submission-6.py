class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_water = 0
        while l < r:
            max_water = max(max_water, min(heights[l], heights[r])*(r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water