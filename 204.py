def countPrimes(self, n: int) -> int:
    if n <= 2:
        return 0
    numbers = [True]*n
    numbers[0], numbers[1] = False, False
    for p in range(2, int(sqrt(n))+1):
        if numbers[p]:
            for multi in range(p*p, n, p):
                numbers[multi] = False
    return sum(numbers)