class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_zeros = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                max_zeros = max(curr, max_zeros)
                curr = 0
        return max(max_zeros, curr)
