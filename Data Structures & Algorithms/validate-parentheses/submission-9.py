class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
            elif not stack:
                return False
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
                continue
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
                continue
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
                continue
            else:
                return False
        return not stack