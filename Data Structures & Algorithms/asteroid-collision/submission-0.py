class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #push to stack
            #only collide if signs are opposite

        stack = []
        for x in asteroids:
            while stack and x < 0 < stack[-1]:
                if stack[-1] < -x:
                    stack.pop()
                    continue
                elif stack[-1] == -x:
                    stack.pop()
                break
            else:
                stack.append(x)
        return stack
            