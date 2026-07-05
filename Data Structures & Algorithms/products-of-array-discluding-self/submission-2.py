class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix-suffix approach, O(2n) -> O(n) time, O(n) space
        output = [1]*len(nums)

        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
