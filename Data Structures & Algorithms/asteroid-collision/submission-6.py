class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
                continue
            else:
                while stack and a < 0 and stack[-1] > 0:
                    if abs(a) < abs(stack[-1]):
                        a = None
                        break
                    elif abs(a) > abs(stack[-1]):
                        stack.pop()
                    else:
                        stack.pop()
                        a = None
                        break
                if a:
                    stack.append(a)
        return stack
