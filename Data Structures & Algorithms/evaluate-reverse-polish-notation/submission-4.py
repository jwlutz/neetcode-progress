class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                two = stack.pop()
                one = stack.pop()
                stack.append(one + two)
            elif t == "-":
                two = stack.pop()
                one = stack.pop()
                stack.append(one - two)
            elif t == "*":
                two = stack.pop()
                one = stack.pop()
                stack.append(one * two)
            elif t == "/":
                two = stack.pop()
                one = stack.pop()
                stack.append(int(one / two))
            else:
                stack.append(int(t))
        return stack.pop()