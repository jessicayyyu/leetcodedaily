def removeKdigits(self, num: str, k: int) -> str:
    stack = []
    for n in num:
        while stack and n < stack[-1] and k:
            stack.pop()
            k -= 1
        if stack or n is not '0':
            stack.append(n)
    if k:
        stack = stack[0:-k]
    return ''.join(stack) or '0'