def myPow(self, x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return self.myPow(1/x, -n)
    if n == 1:
        return x
    res = self.myPow(x, n//2)
    res *= res
    if n%2 == 1:
        res = res*x
    return res
