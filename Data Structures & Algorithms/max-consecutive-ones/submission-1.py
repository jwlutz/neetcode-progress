class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                max_ones = max(max_ones, curr)
                curr = 0
        return max(max_ones, curr)