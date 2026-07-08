class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            if tuple(chars) in groups:
                groups[tuple(chars)].append(s)
            else:
                groups[tuple(chars)] = [s]
        return list(groups.values())
