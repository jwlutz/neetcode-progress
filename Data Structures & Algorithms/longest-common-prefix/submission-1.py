class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for s in strs:

            counter = min(len(res), len(s))
            for i in range(0, counter):
                if res[i] == s[i]:
                    continue
                else:
                    res = res[0:i]
                    break
            res = res[0:counter]
        
        return res

                