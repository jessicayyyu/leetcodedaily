def trap(self, height: List[int]) -> int:
    res, stack = 0, []
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            pre = stack.pop()
            if not stack:
                break
            minHeight = min(height[i], height[stack[-1]])
            res += (minHeight-height[pre])*(i-stack[-1]-1)
        stack.append(i)
    return res


