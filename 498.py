def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    result = []
    if not mat:
        return result
    dd = defaultdict(list)
    m, n = len(mat), len(mat[0])
    for i in range(m):
        for j in range(n):
            dd[i+j].append(mat[i][j])
    for k, v in dd.items():
        if k%2 == 0:
            dd[k].reverse()
        result += dd[k]
    return result