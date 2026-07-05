class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in groups:
                groups[tuple(count)].append(s)
            else:
                groups[tuple(count)] = [s]
        return list(groups.values())