class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if pairs[curr] == c:
                    continue
                else:
                    return False
        return not stack