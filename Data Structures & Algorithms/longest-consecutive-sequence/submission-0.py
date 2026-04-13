class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use frequency map
        seen = set()
        starts = []
        for num in nums:
            seen.add(num)
            if num - 1 not in nums:
                starts.append(num)
        res = 0
        for s in starts:
            curr_len = 1
            curr_num = s + 1
            while curr_num in seen:
                curr_len += 1
                curr_num += 1
            res = max(res, curr_len)
        return res