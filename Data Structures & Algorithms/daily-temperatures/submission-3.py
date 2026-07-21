class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((i, t))
            elif stack[-1][1] < t:
                if not stack:
                    continue
                while stack[-1][1] < t:
                    tmp = stack.pop()
                    result[tmp[0]] = i-tmp[0]
                    if not stack or stack[-1][1] >= t:
                        break
            stack.append((i, t))
        return result
