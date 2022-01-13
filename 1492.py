def kthFactor(self, n: int, k: int) -> int:
    root = int(sqrt(n))
    divider, quote = [], []
    for num in range(1, root + 1):
        if n%num == 0:
            divider.append(num)
            quote.append(n//num)
    if divider[-1] == quote[-1]:
        quote.pop()
    factors = divider + quote[::-1]
    if len(factors) < k:
        return -1
    else:
        return factors[k-1]