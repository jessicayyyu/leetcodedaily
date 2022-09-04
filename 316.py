def removeDuplicateLetters(self, s: str) -> str:
    stack = []
    last = {c: i for i, c in enumerate(s)}
    for i, c in enumerate(s):
        if c in stack:
            continue
        while stack and c < stack[-1] and i < last[stack[-1]]:
            stack.pop()
        stack.append(c)
    return "".join(stack)