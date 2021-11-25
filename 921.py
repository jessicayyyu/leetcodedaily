def minAddToMakeValid(self, s: str) -> int:
    left, right = 0, 0
    for i in s:
        if right == 0 and i == ')':
            left += 1
        else:
            if i == '(':
                right += 1
            else:
                right -= 1
    return left + right