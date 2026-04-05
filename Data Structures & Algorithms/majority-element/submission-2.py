class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num in elements:
                elements[num] += 1
                if elements[num] > (len(nums) / 2):
                    return num
            else:
                elements[num] = 1