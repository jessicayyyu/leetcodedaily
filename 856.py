def scoreOfParentheses(self, s: str) -> int:
    cur = 0
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(cur)
            cur = 0
        else:
            cur = stack.pop() + max(2*cur, 1)
    return cur