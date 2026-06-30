class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elements = {}
        for i in range(len(s)):
            if s[i] in elements:
                elements[s[i]] += 1
            else:
                elements[s[i]] = 1
            if t[i] in elements:
                elements[t[i]] -= 1
            else:
                elements[t[i]] = -1

        return all(v == 0 for v in elements.values())