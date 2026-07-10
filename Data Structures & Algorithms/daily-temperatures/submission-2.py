class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            #push i to the stack so that we can find difference in days

            while stack and t > stack[-1][1]:
                out = stack.pop()
                result[out[0]] = i - out[0]
            stack.append((i, t))
        return result