class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputs = []
        nums.sort()
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                
                if (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
                elif (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (nums[i] + nums[l] + nums[r]) == 0:
                    if [nums[i], nums[l], nums[r]] not in outputs:
                        outputs.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        continue
                    l += 1
                    r -= 1

        return outputs
            


