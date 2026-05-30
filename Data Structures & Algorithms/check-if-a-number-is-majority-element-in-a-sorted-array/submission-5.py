class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        first = hi
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] >= target:
                first = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return first + len(nums) // 2 < len(nums) and nums[first + len(nums) // 2] == target
            
        
        