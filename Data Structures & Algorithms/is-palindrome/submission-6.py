class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = s.strip().lower()
        l, r = 0, len(cleaned)-1
        while l < r:
            if not cleaned[l].isalnum():
                l += 1
            elif not cleaned[r].isalnum():
                r -= 1
            elif cleaned[l] != cleaned[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        