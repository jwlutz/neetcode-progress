class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1
            if t[i] in chars:
                chars[t[i]] -= 1
            else:
                chars[t[i]] = -1
            
        return all(v == 0 for v in chars.values())