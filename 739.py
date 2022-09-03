def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    stack, res = [], [0]*n
    for i in range(n-1, -1, -1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res