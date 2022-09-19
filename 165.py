def compareVersion(self, version1: str, version2: str) -> int:
    num1 = version1.split('.')
    num2 = version2.split('.')
    n1, n2 = len(num1), len(num2)
    for i in range(max(n1, n2)):
        i1 = int(num1[i]) if i < n1 else 0
        i2 = int(num2[i]) if i < n2 else 0
        if i1 != i2:
            if i1 > i2:
                return 1
            else:
                return -1
    return 0