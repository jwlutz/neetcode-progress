class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(index, remaining_target):
            if remaining_target == 0:
                result.append(list(subset))
                return
            if remaining_target < 0 or index == len(nums):
                return

            subset.append(nums[index])
            backtrack(index, remaining_target - nums[index])
            subset.pop()
            backtrack(index + 1, remaining_target)
        backtrack(0, target)
        return result