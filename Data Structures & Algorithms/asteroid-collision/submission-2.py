class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0 or not stack:
                stack.append(a)
                continue

            elif a < 0 and stack[-1] > 0:
                while stack and a < 0 < stack[-1]:
                    if abs(a) > abs(stack[-1]):
                        stack.pop()
                        continue
                    elif abs(a) == stack[-1]:
                        stack.pop()
                    break
                else:
                    stack.append(a)
            else:
                stack.append(a)
        return stack