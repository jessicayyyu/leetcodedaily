from collections import deque
d=[(1,0),(-1,0),(0,1),(0,-1)]
def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    q = deque([(start[0], start[1])])
    visited = set()
    while q:
        x, y = q.popleft()
        visited.add((x, y))
        if x == destination[0] and y == destination[1]:
            return True
        for dx, dy in d:
            nx, ny = x, y
            while self.isValid(maze, nx+dx, ny+dy):
                nx, ny = nx + dx, ny + dy
            if maze[nx][ny] == 0 and (nx, ny) not in visited:
                q.append((nx, ny))
    return False

def isValid(self, grid, x, y):
    m, n = len(grid), len(grid[0])
    return 0<= x< m and 0 <= y < n and grid[x][y]==0
