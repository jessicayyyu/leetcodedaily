def largestRectangleArea(self, heights: List[int]) -> int:
    heights.append(0) #deal with boundary, consider increasing heights list, no res calculation occurs until hits added 0
    res, stack = 0, []
    for i in range(len(heights)):
        while stack and heights[i] <= heights[stack[-1]]:
            preHeight = heights[stack.pop()]
            if not stack:
                width = i #as we start from 0 for index
            else:
                width = i - stack[-1] - 1
            res = max(res, preHeight*width)
        stack.append(i)
    return res
