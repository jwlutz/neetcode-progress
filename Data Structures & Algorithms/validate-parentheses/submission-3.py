class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
                continue
            if not stack:
                return False
            elif stack and (s[i] == ')' and stack[-1] == '('):
                stack.pop()
            elif stack and (s[i] == ']' and stack[-1] == '['):
                stack.pop()
            elif stack and (s[i] == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                return False
        return not stack