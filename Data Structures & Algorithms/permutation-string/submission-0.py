class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #2 hashmaps
        #fill out first one, iterate through second one
        #check equality, if not equal remove left then add right
        #make sure to check bounds and length inequality correctly
        #checking if s2 contains a permutation of s1
        if len(s1) > len(s2):
            return False
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1

        l = 0
        for r in range(len(s2)):
            if s2[r] in freq:
                freq[s2[r]] -= 1
            if all(v == 0 for v in freq.values()):
                return True
            if (r-l+1) >= len(s1):
                if s2[l] in freq:
                    freq[s2[l]] += 1
                l += 1
            
        return False
                
