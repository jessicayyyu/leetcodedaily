def findBuildings(self, heights: List[int]) -> List[int]:
    stack = []
    stack.append(len(heights) - 1)
    for i in range(len(heights)-2, -1, -1):
        if heights[i] > heights[stack[-1]]:
            stack.append(i)
    stack.reverse()
    return stack