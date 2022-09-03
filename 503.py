def nextGreaterElements(self, nums: List[int]) -> List[int]:
    n = len(nums)
    stack, res = [], [0]*n
    for i in range(2*n-1, -1, -1):
        while stack and nums[i%n] >= stack[-1]:
            stack.pop()
        if not stack:
            res[i%n] = -1
        else:
            res[i%n] = stack[-1]
        stack.append(nums[i%n])
    return res