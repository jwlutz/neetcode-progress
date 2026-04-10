class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            #remove chars from the left until no dupes
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len