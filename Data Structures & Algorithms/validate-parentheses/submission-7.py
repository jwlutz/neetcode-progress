class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if not stack and s[i] not in ('(', '[', '{'):
                return False
            elif s[i] in ('(', '[', '{'):
                stack.append(s[i])
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return not stack
            