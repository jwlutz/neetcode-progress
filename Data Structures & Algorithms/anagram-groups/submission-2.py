class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #compare by creating 26-length vectors of counts
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
