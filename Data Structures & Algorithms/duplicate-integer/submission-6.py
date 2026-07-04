class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for num in nums:
            if num in elements:
                return True
            else:
                elements.add(num)
        return False