def calculate(self, s: str) -> int:
    res = 0
    num = 0
    num_ch = 0
    sign = '+'
    stack = []

    for ch in s:
        num_ch += 1
        if ch.isdigit():
            num = 10 * num + int(ch)

        if ch != ' ' and not ch.isdigit() or num_ch == len(s):
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            if sign == '*':
                last_num = stack.pop()
                stack.append(last_num * num)
            if sign == '/':
                last_num = stack.pop()
                stack.append(int(last_num / num))
            sign = ch
            num = 0

    for num in stack:
        res += num

    return res