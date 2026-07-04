class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                ones = max(ones, curr)
                curr = 0
        return max(ones, curr)