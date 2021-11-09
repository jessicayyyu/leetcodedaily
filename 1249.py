def minRemoveToMakeValid(self, s: str) -> str:
    stack = []
    cur = ''
    for c in s:
        if c.isalpha():
            cur += c
        elif c == '(':
            stack.append(cur)
            cur = ''
        else:
            if stack:
                cur = stack.pop() + '(' + cur + ')'
    while stack:
        cur = stack.pop() + cur
    return  cur



