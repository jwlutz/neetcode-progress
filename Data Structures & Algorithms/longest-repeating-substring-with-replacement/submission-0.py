class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_len = 0
        l = 0
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            while (r-l +1 - max(freq.values())) > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, (r-l + 1))
        return max_len
        