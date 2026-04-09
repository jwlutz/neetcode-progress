class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = [1]*len(nums)
        for i, num in enumerate(nums):
            for j in range(len(outputs)):
                if i == j:
                    continue
                else:
                    outputs[j] *= num
        return outputs